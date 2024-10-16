import cv2

def adaptive_threshold(image, max_value, adaptive_method, threshold_type, block_size, C):
    
    if image is None or image.size == 0:
        raise ValueError("Input image is empty.")

    # apply adaptive thresholding to the input image.
    return cv2.adaptiveThreshold(image, max_value, adaptive_method, threshold_type, block_size, C)

