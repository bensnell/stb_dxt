#!/usr/bin/env python2

from stb_dxt import *
from PIL import Image
import numpy as np

img = Image.open("example_assets/dog.jpg")
if compress_image_to_file(img, "example_assets/dog.dxt"):
	print("Successfully converted image to dxt.")
else:
	print("Could not convert image to dxt.")