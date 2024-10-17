import unittest
from pyaip.noise_reduction import gaussian_blur
from PIL import Image
import numpy as np

class TestNoiseReduction(unittest.TestCase):
    def test_gaussian_blur(self):
        
        # create a simple test image (white square)
        image = Image.new("RGB", (100, 100), "white")

        # convert to OpenCV format (numpy array)
        image_cv = np.array(image)

        # apply gaussian blur
        blurred_image = gaussian_blur(image_cv, (5, 5), 0)

        # ensure the output is an image
        self.assertIsInstance(blurred_image, np.ndarray)

        # check the shape to see if it's still the same size
        self.assertEqual(blurred_image.shape, (100, 100, 3))

if __name__ == '__main__':
    unittest.main()