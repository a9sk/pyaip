import cv2
import numpy as np

def gaussian_blur(image, kernel_size=(5, 5), sigma=1):
    
    if image is None or image.size == 0:
        raise ValueError("Input image is empty.")
    
    # apply gaussian blur to the image to reduce noise.
    return cv2.GaussianBlur(image, kernel_size, sigma)

def median_filter(image, kernel_size=5):
    
    # apply median filtering to remove salt-and-pepper noise.
    return cv2.medianBlur(image, kernel_size)
