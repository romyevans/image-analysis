# Image Analysis

This repository provides code to assist in measuring vascular density in images of brain regions. This readme serves as a guide of how to use this code to perform your own analysis.

### Vessel Count & Average Vessel Width
To run the analysis, first modify the settings in `process_image.py` to use the correct folder and images. You can also set optional scaling of the image to improve performance of the code. However, this comes at the expense of image fidelity, defaults to 0.4.

The code expects two inputs, the `folder_name` and the `image_name` these should be set according to the structure below, where the folder name is the path relative to `process_image.py`. 
```
project
│   README.md
│   process_image.py
│   ...
│
└─── <folder_name>
│   │   <image_name_1>
│   │   <image_name_2>
│   │   ...
```

```python
# Read jpg image
folder_name = 'Image Folder'
image_name = 'image_name.jpg'
```
Once configure the code can then be run, this will create an interactive pyplot window with three sliders for:
1. Sigma - the "length scale" which the edge detection algorithm will use. This should be set such that the fine details of each vessel is captured by the outline, but no further otherwise spurious elements will be included.
2. Size - the minimum size of an acceptable vessel, this will remove small regions of noise which are present. Regions smaller than this threshold will be ignored.
3. Mask - The minimum acceptable pixel intensity value, intensity values below this threshold are ignored when considering the edges of regions. This is useful for removing bacground artefacts. 

Once set, the view will recalculate and display the results of average vessel width and number of vessels. The number of vessels can be used to deterime the vessel density by dividing by the image area.