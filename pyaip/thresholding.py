import cv2

def adaptive_threshold(image, max_value=255, block_size=11, C=2):
    """
    Apply adaptive thresholding to convert image to binary.
    
    Args:
        image: numpy.ndarray, Grayscale input image
        max_value: int, Maximum value for pixels
        block_size: int, Size of pixel neighborhood (must be odd)
        C: int, Constant subtracted from mean
    
    Returns:
        numpy.ndarray: Binary image
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    # Ensure block size is odd
    block_size = block_size if block_size % 2 == 1 else block_size + 1
    
    return cv2.adaptiveThreshold(
        image,
        max_value,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        block_size,
        C
    )

