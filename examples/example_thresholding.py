import cv2
from pyaip.thresholding import adaptive_threshold
from pyaip.utils import load_image, save_image

image = load_image('data/test_image.png')

# apply adaptive threshold
thresholded_image = adaptive_threshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
save_image(thresholded_image, 'data/thresholded_image.png')