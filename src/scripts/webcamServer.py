import socketserver
from typing import Tuple
import pyshine
import cv2
import logging
from datetime import datetime
import json

class WebcamServer(pyshine.StreamProps):
    capture_directory = ''
    capture_camera = ''
    def do_GET(self):
        '''
        I am overriding the pyshine.StreamProps do_GET function to respond to requests on /photo. The do_GET function is native to the http.server.BaseRequestHandler module and it is used to handle GET requests
        '''
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = self.PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            if self.mode == 'cv2':
                try:
                    while True:
                        rc,img = self.capture.read()
                        
                        frame = cv2.imencode('.JPEG', img,[cv2.IMWRITE_JPEG_QUALITY,self.quality])[1].tobytes()
                        self.wfile.write(b'--FRAME\r\n')
                        self.send_header('Content-Type', 'image/jpeg')
                        self.send_header('Content-Length', len(frame))
                        self.end_headers()
                        self.wfile.write(frame)
                        self.wfile.write(b'\r\n')
                except Exception as e:
                    logging.warning(
                        'Removed streaming client %s: %s',
                        self.client_address, str(e))
        elif self.path == '/photo':
            try:
                # now = str(datetime.now()).replace(':', '').replace(' ', '-')
                path = f'{self.capture_directory}'
                determinerNumber = 1
                determiner = "img" + str(determinerNumber) + ".png"
                determiner = path + determiner
                bool = True
                while bool:
                    try:
                        f = open(determiner)
                        determinerNumber += 1
                        determiner = "img" + str(determinerNumber) + ".png"
                        determiner = path + determiner
                        f.close()
                    except IOError:
                        bool = False
                inter = open("./inter.txt", "w")
                inter.write(str(determinerNumber))
                inter.close()
                now = "img" + str(determinerNumber)
                path = f'{self.capture_directory}{now}.png'
                rc,img = self.capture.read()
                cv2.imwrite(path, img)

                content = json.dumps({
                    "Success": True,
                    "Photo Name" : now,
                    "Photo Path" : path,
                    "Photo Index" : determinerNumber
                })
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                # self.send_header('Content-Length', len(content))
                self.send_header('Access-Control-Allow-Origin', '*')

                self.end_headers()
                self.wfile.write(content.encode('utf-8'))


                print(f'Photo taken with name {now}')
                # self.send_response(200)
            except Exception as e:
                print(e)

        else:
            self.send_error(404)
            self.end_headers()
