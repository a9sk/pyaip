# import the main functions from each module to make them accessible from the top-level package

from .noise_reduction import gaussian_blur, median_filter
from .thresholding import adaptive_threshold
from .skew_correction import detect_skew_angle, rotate_image, correct_skew
from .line_detection import detect_text_lines

__all__ = [
    'gaussian_blur', 
    'median_filter',
    'adaptive_threshold',
    'detect_skew_angle',
    'rotate_image',
    'correct_skew'
    'detect_text_lines',
]
