#!/usr/bin/env python
# coding: utf-8

# # Computer Vision Quickstart for Microsoft Azure Cognitive Services. 
# Uses remote image(s) in this example. This notebooks runs on Anaconda (2.6+ tested) package Notebook services, with all below listed python modules installed.
# 
# Original source: https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py
# 
# Modified content.
# 
# Prerequisites:
#     - Have or create an Azure Computer Vision service (key, endpoint) here: https://portal.azure.com/
#       follow this: https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=windows%2Cvisual-studio&pivots=programming-language-python
#     - Azure Cognitive Services, Computer vision SDK
#       pip install --upgrade azure-cognitiveservices-vision-computervision
#     - Install PIL:
#       pip install --upgrade pillow
#     - find publicly available (free to use) images online
#       advice: small images around 400-600 px are fine, use reasonable resource and analyse faster than HD images
#       
# Created on Tue Dec 24 14:39:58 2024
# 
# @author: josesan77

# In[5]:


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


# <snippet_client>
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# </snippet_client>
"""
END - Authenticate
"""


# In[35]:


"""
Quickstart variables
These variables are shared by several examples
"""
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
#images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
# <snippet_remoteimage>
remote_image_url = "https://cdn.pixabay.com/photo/2024/01/04/21/54/volcano-8488486_640.jpg"
#"https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png" 
#"https://media.istockphoto.com/id/1987655119/de/foto/smiling-young-businesswoman-standing-in-the-corridor-of-an-office.jpg?b=1&s=612x612&w=0&k=20&c=bGj5izPPSuOWUuVH8Y2O-Hpai9JJIul-MiBNFSDGfwo=" 
#"https://cdn.pixabay.com/photo/2023/12/19/21/52/trees-8458466_960_720.jpg"
#"https://cdn.pixabay.com/photo/2024/01/04/21/54/volcano-8488486_640.jpg" # 'outdoor_mountain' with confidence 89.45%

# </snippet_remoteimage>
"""
END - Quickstart variables
"""


# Verify remote image url

# In[20]:


remote_image_url


# In[34]:


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
print()


# In[36]:


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
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))

# Adult content
# Print results with adult/racy score
print("Analyzing remote image for adult or racy content ... ")
print("Is adult content: {} with confidence {:.2f}".format(results_remote.adult.is_adult_content, results_remote.adult.adult_score * 100))
print("Has racy content: {} with confidence {:.2f}".format(results_remote.adult.is_racy_content, results_remote.adult.racy_score * 100))
# </snippet_adult>
print()


# In[ ]:




