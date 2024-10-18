import cv2
from pyaip.noise_reduction import gaussian_blur, median_filter
from pyaip.utils import load_image, save_image

image = load_image('data/test_image.png')

blurred_image = gaussian_blur(image, kernel_size=(5, 5), sigma=1.0)
save_image(blurred_image, 'data/blurred_image.png')

filtered_image = median_filter(image)
save_image(filtered_image, 'data/filtered_image.png')