# -*- coding: utf-8 -*-
"""
Computer Vision Quickstart for Microsoft Azure Cognitive Services. 
Uses local image(s) in this example.

Source: https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py

Modified content.

Prerequisites:
    - Have or create an Azure Computer Vision service (key, endpoint) here: https://portal.azure.com/
      follow this: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python
    - Azure Cognitive Services, Computer vision SDK
      pip install --upgrade azure-cognitiveservices-vision-computervision
    - Install PIL:
      pip install --upgrade pillow
    - Create folder and collect images: 
      If you don't download the complete package including all folders and content
      then create a subfolder called "images" in the same folder as this script.
      Go to this website to download images:
        https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images
      Add the following 7 images (or use your own) to your "images" folder: 
        faces.jpg, gray-shirt-logo.jpg, handwritten_text.jpg, landmark.jpg, 
        objects.jpg, printed_text.jpg and type-image.jpg
        or using a batch link downloader using the follwoing links:
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/celebrities.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/dog.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/faces.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/landmark.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/landmark.png?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/house.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/objects.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/MultiPageHandwrittenForm.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/cheese_clipart.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/gray-shirt-logo.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/hadwritten_text.png?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/printed_handwritten.jpg?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/printed_text.png?raw=true
        www.github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/ComputerVision/Images/type-image.jpg    
        
Created on Tue Dec 24 14:39:58 2024

@author: josesan77
"""

# <snippet_imports_and_vars>
# <snippet_imports>
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
# from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes, Details
from msrest.authentication import CognitiveServicesCredentials

import os

""" optionally useful modules
from array import array
from PIL import Image
import sys
import time
"""
# </snippet_imports>


'''
Authenticate
Authenticates your credentials and creates a client.
'''
# <snippet_vars>
# do not share key and endpoint values, keep it confidential!
subscription_key = "PASTE_YOUR_COMPUTER_VISION_KEY_HERE"
endpoint = "https://PASTE_YOUR_COMPUTER_VISION_ENDPOINT_HERE.cognitiveservices.azure.com/"
# </snippet_vars>
# </snippet_imports_and_vars>


# <snippet_client>
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# </snippet_client>
"""
END - Authenticate
"""

"""
Quickstart variables
These variables are shared by several examples
"""
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
# <snippet_remoteimage>
remote_image_url = "https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png"
# </snippet_remoteimage>
"""
END - Quickstart variables
"""

'''
Describe an Image - local
This example describes the contents of an image with the confidence score.
'''
print("===== Describe an Image - local file =====")
# Open local image file
img_filename = "faces.jpg" # use one of the above given image filenames
local_image_path = os.path.join (images_folder, img_filename)
local_image = open(local_image_path, "rb")

"""  lion_draing.png
# 'abstract_nonphoto' with confidence 99.61%
""" 

""" faces.jpg
'person' with confidence 99.89%
'human face' with confidence 99.74%
'smile' with confidence 99.20%
'outdoor' with confidence 98.60%
'happy' with confidence 96.98%
'clothing' with confidence 96.16%
'friendship' with confidence 94.64%
'tree' with confidence 91.73% - Note that this is wrong classification!
'female person' with confidence 89.10%
'girl' with confidence 88.87%
'social group' with confidence 87.20%
'posing' with confidence 86.55%
'adolescent' with confidence 85.74%
'love' with confidence 85.26%
'laugh' with confidence 85.01%
'people' with confidence 84.99%
'lady' with confidence 84.45%
'woman' with confidence 81.82%
'group' with confidence 79.30%
'wedding' with confidence 61.53%
'dress' with confidence 51.72%
"""


'''
Tag an Image - local
This example returns a tag (key word) for each thing in the image.
'''
print("===== Tag an Image - local file =====")
# Open local image file
local_image = open(local_image_path, "rb")
# Call API local image
tags_result_local = computervision_client.tag_image_in_stream(local_image)

# Print results with confidence score
print("Tags in the local image: ")
if (len(tags_result_local.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_local.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
'''
END - Tag an Image - local
'''