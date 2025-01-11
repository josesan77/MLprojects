# MLprojects - SciKit Image
Collection of image processing projects, using different *SciKit image* tools, notebooks, info

![Segmentations](./images/segmentations_selected.png)

# SciKit image python module

This directory contains projects on *SciKit Image* library to process/manipulate images. 

The original notebooks can be found here: [SciKit Image ML examples (GitHub)](https://github.com/scikit-image/skimage-tutorials/)

These Python library is built on top of *NumPy*, *SciPy* for **image processing and analysis**, and use Matplotlib for final visualization. While it is not explicitly an ML library, it integrates well with machine learning frameworks like *scikit-learn* for creating pipelines that involve image processing and machine learning.

## Features of Scikit-Image:
- Preprocessing: Denoising, rescaling, thresholding, and normalization of images.
- Feature Extraction: Identifying edges, textures, and regions of interest in images.
- Segmentation: Dividing an image into meaningful regions for analysis.
- Transformation: Geometric transformations, color manipulation, and filtering.
- Visualization: Tools to display and analyze processed images.

## Applications in Machine Learning
1 Image Classification
1 Object Detection and Recognition
1 Medical Imaging
1 Computer Vision (CV) applications
1 Content-Based Image Retrieval (CBIR)

Notebooks included are free-to-use, similar to the intention of the originals, and has easy-access services involved. For other tutorials visit the Github resource!

# Elaboration, diversification and upgrades
I have elaborated the tutorial notebooks, completed the missing parts and went further; I added further explanations (text and images), detailed the steps and added content to each notebook. I also made several attempts on some topics to verify the limits of the tools varying the target images which of course required optimization of the process: using different [SciKit Image filtering tpyes](https://scikit-image.org/docs/dev/api/skimage.filters.html), and different approach in each case.

The examples may be reused, tested, but I encourage everyone to make his/her own project using your own choice of image. Select from the [Skimage image dataset](https://scikit-image.org/docs/dev/auto_examples/data/plot_general.html#sphx-glr-auto-examples-data-plot-general-py) or use your own, as you like.

In general links to the original service providers are provided, but web search can easily drop you to the right place, if link is not given/broken.

# Usage and requirements

## Google Colaboratory (Colab)
As Colab has Numpy, SciPy, and Skimage modules preinstalled, the 
```
import skimage
```
command is enough.

## On PC/Laptop
Using Anaconda or other python distribution, Jupyter Lab or Jupyter Notebook is available. Please ensure that skimage module is installed, verify the presence of the package from a notebook / python environment:
```
import skimage as ski
print(ski.__version__)
```
or, from the command line:
```
python -c "import skimage; print(skimage.__version__)"
```
and install if not present (from command line):
```
python -m pip install -U scikit-image
python -m pip install -U scikit-image[data]
```
The latter one is for the image sample dataset a well selected starter set to learn and play around.

Have fun!