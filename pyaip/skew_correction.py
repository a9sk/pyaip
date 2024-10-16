import cv2
import numpy as np

def detect_skew_angle(image):

    # detect the skew angle of the text in an image using Hough Line Transform.
    edges = cv2.Canny(image, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    angles = []
    if lines is not None:
        for line in lines:
            for rho, theta in line:
                angle = np.degrees(theta) - 90
                angles.append(angle)
    
    return np.median(angles) if angles else 0

def rotate_image(image, angle):

    # rotate the image to correct the skew.
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def correct_skew(image):

    # correct skew in the input image using Hough Transform.
    if image is None or image.size == 0:
        raise ValueError("Input image is empty.")
    angle = detect_skew_angle(image)
    rotated_image = rotate_image(image, angle)
    
    return rotated_image
