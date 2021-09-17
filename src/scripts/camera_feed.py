import cv2
import  pyshine as ps
from webcamServer import WebcamServer

PHOTO_DIRECTORY = r'../interface/camera1/'

HTML="""
<html>
<body>
<img src="stream.mjpg" style="width: 100%; height: 100%;" autoplay playsinline>
</body>
</html>
"""


def main(camera):
    StreamProps = WebcamServer
    StreamProps.set_Page(StreamProps,HTML)
    StreamProps.capture_directory = PHOTO_DIRECTORY
    StreamProps.capture_camera = camera
    address = ('0.0.0.0', 9000) #We have to add the JetSon's ip
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(camera)
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,360)
        capture.set(cv2.CAP_PROP_FPS,15)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()
        
    except KeyboardInterrupt:
        print("\nReceived Keyboard Interrupt, exiting...")
        capture.release()
        server.socket.close()
        
if __name__=='__main__':
    main(1)
