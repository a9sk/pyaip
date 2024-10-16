import cv2

def detect_text_lines(image):
    
    # detect text lines using morphological operations.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 5))
    dilated = cv2.dilate(image, kernel, iterations=1)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours
