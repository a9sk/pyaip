import unittest
import numpy as np
import cv2
from pyaip import adaptive_threshold

class TestAdaptiveThresholding(unittest.TestCase):
    def test_adaptive_threshold(self):
        # create a simple grayscale test image (black square on white background)
        image = np.ones((100, 100), dtype=np.uint8) * 255
        cv2.rectangle(image, (25, 25), (75, 75), (0, 0, 0), -1)

        # apply adaptive thresholding
        thresh_image = adaptive_threshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # ensure the output is an image (numpy array)
        self.assertIsInstance(thresh_image, np.ndarray)

        # check that the output is the same shape as the input
        self.assertEqual(thresh_image.shape, image.shape)

        # check for expected values in the thresholded image
        unique_values = np.unique(thresh_image)
        self.assertTrue(set(unique_values).issubset({0, 255}))

if __name__ == "__main__":
    unittest.main()
