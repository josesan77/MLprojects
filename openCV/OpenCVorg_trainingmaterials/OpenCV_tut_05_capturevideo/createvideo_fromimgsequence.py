# -*- coding: utf-8 -*-
"""
Create a video from a sequence of images using OpenCV

base code source from: OpenCV tutorial. https://docs.opencv.org/
Modified by: josesan77

Functionality:
This script creates a video from a sequence of images using OpenCV (Python module). All images must be placed in the same directory as this script, and are in '.jpg' format.
This is a simple application without GUI and neither video recording nor interactive modification functionality is included.

The naming convention for the images is 'img_01.jpg', 'img_02.jpg', 'img_03.jpg', etc. if 'img_%02d.jpg' is used in the code. '%02d' is a placeholder for the image sequence number with 2 digit serial number.
Numbering should start from 01, and the sequence should be continuous without any missing numbers.

Some images are included in the repository for testing purposes. You can use your own images as well. Check image format compatibility with OpenCV.

Steps:
Import required libraries (cv2 for OpenCV and sys for system functions).
Set the default camera device index to 0. Check for user-specified device index; defaulting to 0 if not provided.
Create a VideoCapture object to interface with the camera.
Open a named display window for the video stream.
Enter a loop to capture frames and display them in real-time.
Exit the loop when the user presses the 'Esc' key on keyboard.

Key Functions:
cv2.VideoCapture(device_index): Captures video from the specified device.
cv2.namedWindow(window_name): Creates a window for display.
cv2.imshow(window_name, frame): Displays a frame in the created window.
cv2.waitKey(2): Captures keyboard events for exit control (at 2 ms intervals).

Error Handling:
If the frame capture fails, the loop will terminate.

WaitKey(200) is used to wait for a 'key event' : button press, for 200 ms, before continuing to the next frame. Press any button to continue to the next frame. The number also defines the frame rate: 200 ms => ~5 FPS. Change the value to adjust the frame rate.
200 ms is set to allow the user to see the frames. If you want to play the video at a faster rate, reduce the value.
Code also prints the frame number on the console.

OpenCV module's C++ documentation (class reference)
https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html

Created on Tue Jan 21 16:00:31 2025

@author: Acer
"""

import cv2
import sys

imSeq = cv2.VideoCapture(r"images\\viff%3d.jpg") # exchange to file path pointing to your image sequence
cv2.namedWindow("Loaded sequence of Images", cv2.WINDOW_NORMAL)

if(imSeq.isOpened() == False):
    print("Error opening the video")
    sys.exit()

counter = 0
while(imSeq.isOpened()):
    ret, frame = imSeq.read()
    print("ret:", ret)
 
    if ret == True:
        cv2.imshow("Frames",frame)
 
        if cv2.waitKey(200): #one frame display time in millisec 40 ms => ~25 FPS
            # a breakpoint, to interactively step the frames, press any key to continue when you like
            #breakpoint() # uncomment to use breakpoint!
            print(counter) #a feedback only, can be removed
            
    else:
        break
    counter += 1 

# Release the video capture object when stream ends
imSeq.release()
cv2.destroyAllWindows()