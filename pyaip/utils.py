import cv2

def load_image(image_path):
    
    # load an image from the file system.
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def save_image(image, output_path):
    
    # save an image to the file system.
    cv2.imwrite(output_path, image)
