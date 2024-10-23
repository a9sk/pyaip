import cv2
import numpy as np

def gaussian_blur(image, kernel_size=(5, 5), sigma=1):
    """
    Apply Gaussian blur to reduce image noise.
    
    Args:
        image: numpy.ndarray, Input image
        kernel_size: tuple, Size of Gaussian kernel (must be odd numbers)
        sigma: float, Gaussian standard deviation
    
    Returns:
        numpy.ndarray: Blurred image
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    kernel_size = tuple(dim if dim % 2 == 1 else dim + 1 for dim in kernel_size)
    return cv2.GaussianBlur(image, kernel_size, sigma)

def median_filter(image, kernel_size=5):
    """
    Apply median filtering to remove salt-and-pepper noise.
    
    Args:
        image: numpy.ndarray, Input image
        kernel_size: int, Size of median filter kernel (must be odd)
    
    Returns:
        numpy.ndarray: Filtered image
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    # Ensure kernel size is odd
    kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1
    return cv2.medianBlur(image, kernel_size)
