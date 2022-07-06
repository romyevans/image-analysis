import utilities as util
import numpy as np
from skimage import measure
import skimage.feature
import cv2


# Adds Fiji colour map
util.register_fiji_cmap_red('imageJ-red-black')
util.register_fiji_cmap_green('imageJ-green-black')

# Read jpg image
folder_name = 'Vessels2'
image_name = 'TS1 DG.jpg'

raw_image_data_red = util.read_image(folder_name, image_name, stack=0, channel=0)

# Scale down the image to improve performance - use with high pixel count images
scaling = 0.4
raw_image_data_red_sample = cv2.resize(raw_image_data_red, [0,0],  fx=scaling, fy=scaling)


# Put pixel values into the range 0 to 256
image_data = (raw_image_data_red_sample / np.max(raw_image_data_red_sample)) * 256

# Run edge detection on corrected image
slides = util.adjustable_detector(image_data)

# Input final values to compute average vessel width
area = 25
sigma = 3
mask = 26

image_adjusted = image_data * (image_data >= mask)

edges0 = skimage.feature.canny(image=image_adjusted, sigma=sigma)
segs0 = measure.regionprops(measure.label(edges0))
qualified_segments = []
all_coords = np.zeros([1, 2])
for seg in segs0:
    if seg.filled_area > area:
        qualified_segments.append(seg)

print(f'Average vessel width: {np.mean([seg.minor_axis_length for seg in qualified_segments])}')
