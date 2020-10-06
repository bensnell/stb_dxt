# DXT Compression in Python

This repository is a python module for compressing and decompressing DXT1 and DXT5 textures in python.

It borrows heavily from [ofxDXT](https://github.com/armadillu/ofxDXT), a library for OpenFrameworks. An important difference between ofxDXT and this module is that ofxDXT saves DXT files with a header indicating image size and DXT type, while this module saves no such header. As a result, the user must keep track of each saved file's image dimensions and DXT type.

This repo can save to both DXT1 (for RGB images) and DXT5 (for RGBA images).

## Dependencies

The following dependencies are not essential, but make the interface between your code and this module significantly easier. The module could be changed slightly to remove these dependencies if they weren't available.

- `numpy`
- `PIL`

## Building

Before you use, make sure that `lib_stb_dxt.so` is present in the repository and built for the correct system. The shared library provided here is for Linux Ubuntu 18.04 64-bit systems. To build on your own system, use the following command:

```bash
cc -fPIC -shared -o libs/lib_stb_dxt.so src/stb_dxt.c
```

## Usage

Use the library as you would any other python module:

```python
from stb_dxt import *
from PIL import Image
import numpy as np

img = Image.open("image.jpg")
compress_image_to_file(img, "compressed.dxt") # Save compressed image to file
```

