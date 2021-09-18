# Panacea
## _The Robot-Nurse!_
Panacea is Team Greece's project competing in the 2021 FIRST Global Challenge "Discover and Recover". 

## Features
Panacea can:
- Move autonomously in any space with the usage of SLAM algorithms
- Measure vital signs in real time, such as oxygen levels, blood pressure, temperature, etc.
- Disinfect rooms with the use of UVC lamps when they are empty

## Development

Panacea has been **designed, constructed** and **programmed** by students between _16 to 18_ years old from all around Greece, chosen based on their *knowledge*, *experience* and *love* for *robotics*. Due to the fact that it is not possible for all us to work together in real life, the prototype of panacea was constructed by the majority of the team *in a span of two weeks*. However, we plan on *improving the first design* so it can be a great fit in today's society. 

## Installation
Panacea **does not have an installation guide yet**, but we plan on making one *once the project is finished!* In the meantime, if you are interested, you can *check out the source code* for *ideas and inspiration* or to *give us feedback!*  

## Robot Description

### Processing Units
The “brains” of panacea is an Nvidia Jetson Nano Developer Kit. We opted for the Jetson since the processes we want to run on it require a lot of RAM and a powerful Graphics Processing Unit(GPU), that are not available on a chip like the raspberry pi. Along with the Jetson, we use an Arduino Uno to connect the oximeter, since the analog ports it is equipped with come in handy.

### Driving Base 
We are using the REV Robotics components to create the driving base as they are one of the best choices available in the market.. We are using 4 HD Hex Motors 40:1 for the holonomic drive system, 4 2M distance sensors to avoid walls as well as the REV Control Hub and Expansion Hub. We achieve the holonomic driving system by having each of the 4 motors angled 45° and by using omnidirectional wheels. The robot can move freely in any direction without the need to rotate, which is useful especially in obstacle avoidance scenarios. The code for the base is written in Java and can be found in this project’s GitHub Repository. 
 
### Camera System 
We are also using two Logitech C270 cameras to capture photos and videos from the robot's perspective. These cameras are connected to an NVIDIA Jetson Nano Devkit that acts as the Central Processing Unit and Server of the robot. To stream the camera feed to an HTML server, we use the OpenCV and the http.server python libraries. When the robot activates, an HTTP Request Handler is started and listens to specific ports. When it receives requests on “/stream.mjpg” the server responds with the encoded images on every frame. On “/photo” it captures a photo using the OpenCV library.

### Oximeter
To measure the heart rate and oxigen concentration we use a sensor connected to an Arduino Uno. Then, we send all data to the Nvidia Jetson via serial port communication. Then, we pass the values through multiple filters to eliminate the chances of wrong measurements. The measurement period may last up to 30 seconds, as the script admits multiple values to make the final results more accurate. 

### Thermal Camera
For the thermal camera, we combine Thermal (IR) and Visible Spectrum (RGB) cameras to detect people in the scene and measure their skin temperature in a contactless manner based on the thermal camera input. We have ordered a FLIR Lepton 3.5 module. The camera offers 160×120 resolution, and it's pretty hard to beat for the price. Additionally, we have ordered a Group Gets Pure Thermal 2 carrier board, which allows us to use an interface with the camera using USB. The most important feature of the lepton is radiometric measurement. This means that with just a few lines of code, we can extract the temperature of every pixel in the image (not all LWIR cameras offer that). To detect fever, it is sufficient to detect faces, and not the entire body outlines of the subjects. We might even get more robust results because the measurement will not be affected by the person's clothing. The corner of the eye is the most reliable region for contactless temperature measurement with IR cameras. That's why we also detect the subject's eyes in the image. We then use the FLIR Module to detect the fever in the specified range.

### Interface
To see the camera feeds and the oximeter readings, the robot runs a static Express server on the local network. There, we can see the output of the camera streams and the constantly refreshing values of the oximeter sensor. We achieve most of that through simple HTML and JS solutions that can be found in our repository, but some require more programmatically intensive solutions, such as the usage of backend python scripts to take photos from the cameras. To see the readings of the oximeter on the interface, we chose to constantly write the current output in a separate HTML file that is displayed in an iframe. The iframe is being reloaded every second through JS so the new readings appear in the interface.

## MIT License

Copyright (c) 2021 Team Greece (gnrt.gr)  
Permission is hereby granted, free of charge, to any person  
obtaining a copy of this software and associated documentation  
files (the "Software"), to deal in the Software without  
restriction, including without limitation the rights to use,  
copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the  
Software is furnished to do so, subject to the following  
conditions:  
  
The above copyright notice and this permission notice shall be  
included in all copies or substantial portions of the Software.  
  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES  
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND  
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT  
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,  
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR  
OTHER DEALINGS IN THE SOFTWARE.  