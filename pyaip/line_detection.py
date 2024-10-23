import cv2
import numpy as np

def detect_text_lines(image):
    """
    Detect text lines in binary image using morphological operations.
    
    Args:
        image: numpy.ndarray, Binary input image
    
    Returns:
        list: List of contours representing text lines
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    # Create horizontal kernel for detecting text lines
    kernel_length = np.array(image).shape[1]//40
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    
    # Apply morphology operations
    dilated = cv2.dilate(image, horizontal_kernel, iterations=1)
    eroded = cv2.erode(dilated, horizontal_kernel, iterations=1)
    
    # Find contours
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on size
    min_width = image.shape[1] * 0.1  # Minimum 10% of image width
    filtered_contours = [cnt for cnt in contours if cv2.boundingRect(cnt)[2] >= min_width]
    
    return sorted(filtered_contours, key=lambda c: cv2.boundingRect(c)[1])  # Sort by y-coordinate
