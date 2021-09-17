FROM python:3

ADD camera_feed.py /
ADD camera_feed2.py /
ADD webcamServer.py /

RUN pip3 install opencv-python
RUN pip3 install pyshine
RUN pip3 install typing

CMD ["python3", "camera_feed.py"]
