# -*- coding: utf-8 -*-
"""
In-built Camera Streaming Documentation

base code source from: OpenCV tutorial. https://docs.opencv.org/
Modified by: josesan77

This script demonstrates how to access the computer's default camera, capture video frames, and display the streaming output in a window.
This is a simple application without GUI and neither video recording nor interactive modification functionality is included.

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

Usage:
Run the script and press the 'Esc' key to exit the streaming window.
OpenCV module's C++ documentation (class reference)
https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html

Created on Tue Jan 21 16:00:31 2025
@author: josesan77
"""

import cv2
import sys

#initialize the application
err = None # error handling
s = 0

# check if user has provided a camera index when running the script from the terminal
if len(sys.argv) > 1: 
    s = sys.argv[1]

try:
    cap = cv2.VideoCapture(s)
except err as Exception:
    print("Error opening the camera: ", err)
    sys.exit()

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()
    
while cv2.waitKey(2) != 27: # Escape button press checked every 2 secs
    has_frame, frame = cap.read()
    if not has_frame:
        break
    # perform any operations/modification on the frame here
    frame = cv2.flip(frame, 0) # flip the frame: 0 - flip vertically, 1 - flip horizontally
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the frame to grayscale
    # Display the frame in the window
    cv2.imshow(win_name, frame)

# Release the video capture object when stream ends
cap.release()
cv2.destroyWindow(win_name) #cv.destroyAllWindows()