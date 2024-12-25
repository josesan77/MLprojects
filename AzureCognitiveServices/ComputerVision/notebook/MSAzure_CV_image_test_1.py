#!/usr/bin/env python
# coding: utf-8

# # Computer Vision Quickstart for Microsoft Azure Cognitive Services. 
# Using _remote image(s)_ in this example. For local image analysis check original source below or python files in the 'python' folder of this github content: https://github.com/josesan77/MLprojects/tree/master/AzureCognitiveServices/ComputerVision
# 
# This notebooks runs on Anaconda (2.6+ tested) package Notebook services (localhost), with all below listed python modules installed in background.
# 
# Original source: https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py
# 
# Modified content.
# 
# Prerequisites:
#     - Have or create an Azure Computer Vision service (key, endpoint) here: https://portal.azure.com/
#     
#     follow this tutorial: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python
#       
#     - Azure Cognitive Services: Computer vision SDK, add module to existing Python environment
#     
#       pip install --upgrade azure-cognitiveservices-vision-computervision
#       
#     - Install PIL module:
#     
#       pip install --upgrade pillow
#       
#     - find publicly available (free to use) images online, ensure that the image url directly points to an image, not to a webpage / image slider / drive folder or similar image sharing
#     
#       Advice: search for small images, around 400-600 px are fine, as this size of image uses acceptable amount of Azure resources and is analysed faster than HD or higher resolution images.
# 
# If below given images are not accessible, find images in images/web_images subfolder to compare images and understand below defined AI responses.
# 
# Created on Tue Dec 24 14:39:58 2024
# 
# @author: josesan77

# In[37]:


# <snippet_imports_and_vars>
# <snippet_imports>
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes, Details
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
# </snippet_imports>


# ## Authenticate
# Authenticates your credentials and creates a client.

# In[6]:


# <snippet_vars>
# do not share key and endpoint values, keep it confidential!
subscription_key = "PASTE_YOUR_COMPUTER_VISION_KEY_HERE"
endpoint = "https://PASTE_YOUR_COMPUTER_VISION_ENDPOINT_HERE.cognitiveservices.azure.com/"
# </snippet_vars>
# </snippet_imports_and_vars>


# In[7]:


computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

"""
END - Authenticate
"""


# In[90]:


"""
Quickstart variables
These variables are shared by several examples
"""
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
#images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
# <snippet_remoteimage>
remote_image_url = "https://cdn.pixabay.com/photo/2023/05/22/10/49/houses-8010401_640.jpg"
# "https://cdn.pixabay.com/photo/2023/05/22/10/49/houses-8010401_640.jpg" # 'outdoor_mountain' with confidence 66.41%
# "https://cdn.pixabay.com/photo/2014/11/02/10/41/plane-513641_640.jpg" # 'sky_sun' with confidence 98.05%
# "https://cdn.pixabay.com/photo/2023/12/06/17/17/street-8434099_1280.jpg" # 'building_' with confidence 27.34%, 'building_doorwindows' with confidence 13.67%, 'outdoor_street' with confidence 30.86%
# "https://media.istockphoto.com/id/1987655119/de/foto/smiling-young-businesswoman-standing-in-the-corridor-of-an-office.jpg?b=1&s=612x612&w=0&k=20&c=bGj5izPPSuOWUuVH8Y2O-Hpai9JJIul-MiBNFSDGfwo=" 
# "https://cdn.pixabay.com/photo/2023/12/19/21/52/trees-8458466_960_720.jpg"
# "https://cdn.pixabay.com/photo/2024/01/04/21/54/volcano-8488486_640.jpg" # 'outdoor_mountain' with confidence 89.45%

# </snippet_remoteimage>
"""
END - Quickstart variables
"""


# Verify remote image url

# In[43]:


remote_image_url


# In[92]:


# use this block with images below, define remote image URL in above cell:
# "https://cdn.pixabay.com/photo/2014/11/02/10/41/plane-513641_640.jpg" # 'sky_sun' with confidence 98.05%
# "https://cdn.pixabay.com/photo/2023/12/06/17/17/street-8434099_1280.jpg" # 'building_' with confidence 27.34%, 'building_doorwindows' with confidence 13.67%, 'outdoor_street' with confidence 30.86%
# "https://media.istockphoto.com/id/1987655119/de/foto/smiling-young-businesswoman-standing-in-the-corridor-of-an-office.jpg?b=1&s=612x612&w=0&k=20&c=bGj5izPPSuOWUuVH8Y2O-Hpai9JJIul-MiBNFSDGfwo=" 
# "https://cdn.pixabay.com/photo/2024/01/04/21/54/volcano-8488486_640.jpg" # 'outdoor_mountain' with confidence 89.45%

# <snippet_features_remote>
print("===== Analyze an image - remote =====")
# Select the visual feature(s) you want.
remote_image_features = [VisualFeatureTypes.categories,VisualFeatureTypes.brands,VisualFeatureTypes.adult,VisualFeatureTypes.color,VisualFeatureTypes.description,VisualFeatureTypes.faces,VisualFeatureTypes.image_type,VisualFeatureTypes.objects,VisualFeatureTypes.tags]
remote_image_details = [Details.landmarks] #Details.celebrities removed from details list
# </snippet_features_remote>

# <snippet_analyze>
# Call API with URL and features
results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features, remote_image_details)

# Print results with confidence score
print("Categories from remote image: ")
if (len(results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))


# In[63]:


remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg"
# or try one of the below listed images (AI responses are included)

# "https://cdn.pixabay.com/photo/2024/11/02/14/12/ai-generated-9169251_640.jpg" # location 262, 45, 353, 136
# Is adult content: False with confidence 3.10, Has racy content: False with confidence 76.35

# "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg" # locations: 117, 211, 186, 280; 259, 206, 320, 267
# Is adult content: False with confidence 0.33; Has racy content: False with confidence 0.39

# "https://cdn.pixabay.com/photo/2016/10/17/19/40/indians-1748464_640.jpg"  location 150, 199, 333, 382;
# Is adult content: False with confidence 0.13; Has racy content: False with confidence 0.30

#"https://media.istockphoto.com/id/1987655119/de/foto/smiling-young-businesswoman-standing-in-the-corridor-of-an-office.jpg?b=1&s=612x612&w=0&k=20&c=bGj5izPPSuOWUuVH8Y2O-Hpai9JJIul-MiBNFSDGfwo="
# 'None' of age None at location 247, 58, 328, 139; Analyzing remote image for adult or racy content ... 
# Is adult content: False with confidence 0.12
# Has racy content: False with confidence 0.25
remote_image_features = [VisualFeatureTypes.categories,VisualFeatureTypes.brands,VisualFeatureTypes.adult,VisualFeatureTypes.color,VisualFeatureTypes.description,VisualFeatureTypes.faces,VisualFeatureTypes.image_type,VisualFeatureTypes.objects,VisualFeatureTypes.tags]
remote_image_details = [Details.landmarks] # Details.celebrities removed from details list
# </snippet_features_remote>

# <snippet_analyze>
# Call API with URL and features
results_remote = computervision_client.analyze_image(remote_image_url , remote_image_features, remote_image_details)

# Detect faces
# Print the results with gender, age, and bounding box
print("Faces in the remote image: ")
if (len(results_remote.faces) == 0):
    print("No faces detected.")
else:
    for face in results_remote.faces:
        if face.gender is not None and face.age is not None:
            pretext = ("'{}' of age {}".format(face.gender, face.age))
        elif face.age is not None:
            pretext = ("age {}".format(face.age))
        elif face.gender is not None:
            pretext = ("'{}' ".format(face.gender))
        else:
            pretext = ('Gender, and age could not be determined')
        print(pretext + " at location (left, top, right, bottom): {}, {}, {}, {}"\
              .format( face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))

# Adult/racy content verification
# Print results with adult/racy score
print("Analyzing remote image for adult or racy content ... ")
print("Is adult content: {} with confidence {:.2f}".format(results_remote.adult.is_adult_content, results_remote.adult.adult_score * 100))
print("Has racy content: {} with confidence {:.2f}".format(results_remote.adult.is_racy_content, results_remote.adult.racy_score * 100))


# ## Detect colors
# ### Print results of color scheme
# For example in case of remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg"
# 
# AI analysis response:
# 
# - Is black and white: False
# - Accent color: 2D485D
# - Dominant background color: Black
# - Dominant foreground color: Brown
# - Dominant colors: ['Black', 'Brown', 'Grey']

# In[64]:


# Detect colors
# Print results of color scheme
print("Getting color scheme of the remote image: ")
print("Is black and white: {}".format(results_remote.color.is_bw_img))
print("Accent color: {}".format(results_remote.color.accent_color))
print("Dominant background color: {}".format(results_remote.color.dominant_color_background))
print("Dominant foreground color: {}".format(results_remote.color.dominant_color_foreground))
print("Dominant colors: {}".format(results_remote.color.dominant_colors))


# ## Detect image type
# Prints type results with degree of accuracy.
# 
# AI response (remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg")
# 
# Type of remote image:
# - Image is not clip art.
# - Image is not a line drawing.

# In[65]:


# Detect image type
# Prints type results with degree of accuracy
print("Type of remote image:")
if results_remote.image_type.clip_art_type == 0:
    print("Image is not clip art.")
elif results_remote.image_type.line_drawing_type == 1:
    print("Image is ambiguously clip art.")
elif results_remote.image_type.line_drawing_type == 2:
    print("Image is normal clip art.")
else:
    print("Image is good clip art.")

if results_remote.image_type.line_drawing_type == 0:
    print("Image is not a line drawing.")
else:
    print("Image is a line drawing")


# # Detect brands
# 
# AI response (remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg") - No brands detected.
# 

# In[66]:


# Detect brands
print("Detecting brands in remote image: ")
if len(results_remote.brands) == 0:
    print("No brands detected.")
else:
    for brand in results_remote.brands:
        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
        brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
        brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))


# ## Detect objects
# Print detected objects results with bounding boxes
# 
# AI response (remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg")
# 
# Detecting objects in remote image:
# - object at location (left, right, top, bottom) 341, 412, 483, 522
# - object at location (left, right, top, bottom) 195, 280, 515, 566
# - object at location (left, right, top, bottom) 289, 363, 507, 558
# - object at location (left, right, top, bottom) 104, 179, 613, 638
# - object at location (left, right, top, bottom) 52, 234, 275, 433
# - object at location (left, right, top, bottom) 54, 281, 163, 622
# - object at location (left, right, top, bottom) 204, 402, 172, 569
# 
# See manually labeled 'children-7934514_640_objects.png' image in notebook/analysed_images folder. Colors are manually selected, yellows 1-2, orange 3-4, blue ones are for frames 5-6-7.
# 
# Note that not all objects have been found by the AI! And yes, humans are considered as objects in this analysis!

# In[69]:


# Detect objects
# Print detected objects results with bounding boxes
print("Detecting objects in remote image:")
if len(results_remote.objects) == 0:
    print("No objects detected.")
else:
    for object in results_remote.objects:
        print("object at location (left, right, top, bottom) {}, {}, {}, {}".format( \
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))


# ## Describe image
# Get the captions (descriptions) from the response, with confidence level
# 
# AI response (remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg")
# 
# Description of remote image: 
# - 'a group of young boys sitting on a bench eating' with confidence 35.92%
# 
# AI response (remote_image_url =  "https://cdn.pixabay.com/photo/2023/05/22/10/49/houses-8010401_640.jpg")
# 
# - 'a building next to a body of water with mountains in the background' with confidence 54.92%

# In[117]:


# Describe image
# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
if (len(results_remote.description.captions) == 0):
    print("No description detected.")
else:
    for caption in results_remote.description.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()


# ## Return tags
# Print results with confidence score
# 
# AI response (remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg")
# 
# Tags in the remote image: 
# - 'clothing' with confidence 99.82%
# - 'human face' with confidence 99.57%
# - 'person' with confidence 99.19%
# - 'toddler' with confidence 99.15%
# - 'footwear' with confidence 97.42%
# - 'ground' with confidence 96.27%
# - 'girl' with confidence 94.14%
# - 'baby' with confidence 92.82%
# - 'outdoor' with confidence 87.84%
# - 'child' with confidence 80.15%
# - 'sitting' with confidence 74.19%
# - 'boy' with confidence 64.80%
# - 'young' with confidence 62.46%
# 
# I am not the right person to judge gender identification, but I do disagree in 'girl', especially that high confidence value. Also on 'baby' and 'toddler' with such high confidence values.

# In[71]:


# Return tags
# Print results with confidence score
print("Tags in the remote image: ")
if (len(results_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in results_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))


# ## Detect landmarks
# 
# To ensure that Landmark content has been defined, run the following command in the cell below:
# 
# results_remote.categories[0].\__dict__
# 
# 1) In case of remote_image_url = "https://cdn.pixabay.com/photo/2023/04/18/08/42/children-7934514_640.jpg"
# 
# {'additional_properties': {},
#  'name': 'people_group',
#  'score': 0.2890625,
#  'detail': None}
#  
# 2) In case of remote_image_url = "https://cdn.pixabay.com/photo/2023/05/22/10/49/houses-8010401_640.jpg"
# 
# {'additional_properties': {},
#  'name': 'outdoor_mountain',
#  'score': 0.6640625,
#  'detail': <azure.cognitiveservices.vision.computervision.models._models_py3.CategoryDetail at 0x1e239ec8b10>}
#  
#  'detail' contains an object and data should be extracted from it 

# In[94]:


results_remote.categories[0].__dict__


# In[95]:


# if in the cell above the 'detail' is not None (empty), run this cell as well to verify 'landmark' content
results_remote.categories[0].detail.__dict__
# response: {'additional_properties': {}, 'celebrities': None, 'landmarks': []} - landmark is not empty if AI finds something


# In[116]:


# Detect landmarks - list all available information
# use case: remote_image_details = [Details.landmarks] #Details.celebrities removed from details list

print("Landmarks in the remote image:")
if len(results_remote.categories) == 0:
    print("No landmarks detected.")
else:
    for category in results_remote.categories:
        if category.__dict__['name']:
            print(category.__dict__)
            print('details: ' + ', '.join(category.detail.__dict__)) # property list
            print(category.detail.__dict__) # property list with values (may be empty)
        else:
            print('No landmark recognised')


# ## Detect celebrities
# This module requires further authentication and access to 'Celebrity recognition' services. Ask for permission at:
# 
# https://aka.ms/celebrityrecognition
# 
# It may require up to 10 days of feedback.
# 
# In case you have access, use this code replacing the appropriate code line above and rerun that cell! 
# 
# remote_image_details = [Details.celebrities, Details.landmarks]

# In[72]:


# Detect celebrities -  run only if all authentication is done,
# and 1Celebrity recognition' access is granted
print("Celebrities in the remote image:")
if (len(results_remote.categories.detail.celebrities) == 0):
    print("No celebrities detected.")
else:
    for celeb in results_remote.categories.detail.celebrities:
        print(celeb["name"])

