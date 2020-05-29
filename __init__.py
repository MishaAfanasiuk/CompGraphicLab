from numpy import array
from PIL import Image

import transformations.edgeDetection as edgeDetection
import transformations.neighborhoodProcessing as neighborhoodProcessing
import transformations.grayLevelTransformation as grayLevelTransformation
import utils

url = 'rick_sanchez.jpg'
original_image = array(Image.open(url).convert('L'))

utils.draw_image(
    original_image,
    grayLevelTransformation.clamp_image_bitmap_to_interval(original_image, 100, 200),
    'Clamped to interval 100-200'
)

utils.draw_image(
    original_image,
    grayLevelTransformation.change_image_bitmap_darkness(original_image, 3),
    'Darker with degree 3'
)

utils.draw_image(
    original_image,
    neighborhoodProcessing.apply_minimum_filter_to_image(original_image),
    'Minimum filter'
)

utils.draw_image(
    original_image,
    neighborhoodProcessing.apply_mean_filter_to_image(original_image),
    'Mean filter'
)

utils.draw_image(
    original_image,
    neighborhoodProcessing.apply_gaussian_filter_to_image(original_image),
    'Gaussian filter'
)

utils.draw_image(
    original_image,
    edgeDetection.perform_laplacian_edge_detection(url),
    'Laplacian edge-detection'
)