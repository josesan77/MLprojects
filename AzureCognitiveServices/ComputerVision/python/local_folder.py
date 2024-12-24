# -*- coding: utf-8 -*-
"""
Checking the existence of 'images' subfolder, relative to the folder of current .py file

Created on Tue Dec 24 14:41:39 2024
@author: josesan77

"""

import os

"""
Quickstart variables
These variables are shared by several examples
"""
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = None

image_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
if os.path.exists(image_folder_path):
    images_folder = image_folder_path

"""
END - Quickstart variables
"""

print(images_folder)