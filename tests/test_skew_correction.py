import unittest
import numpy as np
import cv2
from pyaip.skew_correction import correct_skew

class TestSkewCorrection(unittest.TestCase):
    def test_correct_skew(self):
        # create a simple skewed image (a rectangle rotated)
        image = np.ones((100, 200), dtype=np.uint8) * 255
        pts = np.array([[50, 10], [150, 10], [160, 90], [40, 90]], dtype=np.int32)
        cv2.fillPoly(image, [pts], (0, 0, 0))

        # apply skew correction
        corrected_image = correct_skew(image)

        # ensure the output is an image (numpy array)
        self.assertIsInstance(corrected_image, np.ndarray)

        # check that the output is the same shape as the input
        self.assertEqual(corrected_image.shape, image.shape)

        # check that the image is not completely white (i.e., some content is preserved)
        self.assertTrue(np.any(corrected_image < 255))

if __name__ == "__main__":
    unittest.main()

