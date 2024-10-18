from setuptools import setup, find_packages

setup(
    name='pyaip',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python-headless',
        'numpy',
        'Pillow',
    ],
    description='Python Image Preprocessing',
    author='a9sk',
    author_email='920a9sk42f76c765@proton.me',
)
