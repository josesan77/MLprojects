# -*- coding: utf-8 -*-
"""
Play a local video file using OpenCV

base code source from: OpenCV tutorial. https://docs.opencv.org/
Modified by: josesan77

This script will play a video file from your local machine using OpenCV (Python module).
The video file this case should be placed in the same directory as this script (unless if correct filepath is defined), and is in '.avi' format.
This is a simple application without GUI and neither video recording nor interactive modification functionality is included.

Steps:

Import required libraries (cv2 for OpenCV and sys for system functions).
Set the default camera device index to 0. Check for user-specified device index; defaulting to 0 if not provided.
Create a VideoCapture object to interface with the camera.
Open a named display window for the video stream.
Enter a loop to capture frames and display them in real-time.
Exit the loop when the user presses the 'q' button on keyboard.

Key Functions:
cv2.VideoCapture(device_index): Captures video from the specified device.
cv2.namedWindow(window_name): Creates a window for display.
cv2.imshow(window_name, frame): Displays a frame in the created window.
cv2.waitKey(2): Captures keyboard events for exit control (at 2 ms intervals).

Error Handling:
If the frame capture fails, the loop will terminate.

WaitKey(2) is used to wait for a 'key event' : button press, for 2 ms, before continuing to the next frame. Press 'q' to quit the video, other buttons won't have effect.
If you want to play a different video file (or use different file location), change the filename in the code.

AVI file is not included in the repository, you can use any .avi file you have on your local machine. Check codec compatibility with OpenCV.

OpenCV module's C++ documentation (class reference)
https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html

@author: Acer
Created on Tue Jan 21 16:30:13 2025
"""

import cv2
 
cap = cv2.VideoCapture('FILEPATHTO.avi') # exchange to file path pointing to your avi file
 
while cap.isOpened() and cv2.waitKey(1) != 27:
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    videocontent = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #use cv2.COLOR_BGR2GRAY to convert to grayscale video 
 
    cv2.imshow('frame', videocontent)
    if cv2.waitKey(2) == ord('q'):
        break

# Release the video capture object when stream ends
cap.release()
cv2.destroyAllWindows()

