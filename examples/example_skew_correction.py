from pyaip.skew_correction import detect_skew_angle, rotate_image
from pyaip.utils import load_image, save_image

image = load_image('data/test_image.png')

# detect the skew angle
angle = detect_skew_angle(image)
print(f"Detected skew angle: {angle} degrees")

# correct the skew
corrected_image = rotate_image(image, angle)
save_image(corrected_image, 'data/corrected_image.png')
