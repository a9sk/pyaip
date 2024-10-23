import cv2
import numpy as np

def detect_skew_angle(image):
    """
    Detect text skew angle using Hough Line Transform.
    
    Args:
        image: numpy.ndarray, Binary input image
    
    Returns:
        float: Detected skew angle in degrees
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    # Apply edge detection
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    
    # Apply Hough transform
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)
    
    if lines is None:
        return 0
    
    angles = []
    for line in lines:
        rho, theta = line[0]
        # Convert theta to degrees and normalize to -90 to 90
        angle = np.degrees(theta) - 90
        if angle < -45:
            angle += 90
        elif angle > 45:
            angle -= 90
        angles.append(angle)
    
    # Return median angle, filtering out outliers
    angles = np.array(angles)
    median_angle = np.median(angles)
    return median_angle

def rotate_image(image, angle):
    """
    Rotate image by specified angle.
    
    Args:
        image: numpy.ndarray, Input image
        angle: float, Rotation angle in degrees
    
    Returns:
        numpy.ndarray: Rotated image
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
        
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Calculate new image dimensions to avoid cropping
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))
    
    # Adjust translation
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]
    
    return cv2.warpAffine(image, M, (new_w, new_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

def correct_skew(image):
    """
    Detect and correct image skew.
    
    Args:
        image: numpy.ndarray, Input image
    
    Returns:
        numpy.ndarray: Deskewed image
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty")
    
    angle = detect_skew_angle(image)
    return rotate_image(image, angle)

