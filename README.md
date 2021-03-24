# DXT Compression in Python

This repository is a python module for compressing and decompressing DXT1 (RGB) and DXT5 (RGBA) textures in python.

It borrows heavily from [ofxDXT](https://github.com/armadillu/ofxDXT), a library for OpenFrameworks. An important difference between ofxDXT and this module is that ofxDXT saves DXT files with a header indicating image size and DXT type, while this module saves no such header. As a result, the user must keep track of each saved file's image dimensions and DXT type.

This library has been confirmed to work on Linux and Windows and comes packaged with libraries for these two platforms.

## Dependencies

The following dependencies are required:

- `Python`

The following dependencies are not essential, but make the interface between your code and this module significantly easier. The module could be changed slightly to remove these dependencies if they weren't available.

- `numpy`
- `Pillow` (requires Python 2.7 32-bit installation)

## Installation

### Install Dependencies

Python installation instructions can be found [here](https://www.python.org/downloads/). A few notes on installing python:

- If installing on Windows and using the Pillow dependency, you must use Python 2.7 32-bit (x86). Use [this link](https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi) to install it.

- Sometimes, Windows has difficulty locating the python executable, so it is recommended to run this command in Powershell after installing Python. This command assumes Python 2.7 has been installed.

  ```bash
  [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
  ```

The recommended, optional dependencies can be installed by running this command for Python2:

```bash
pip2 install Pillow numpy
```

### Install Module

The module has not yet been setup as an official Python module with [setuptools](https://setuptools.readthedocs.io/en/latest/) support. However, this does not mean that it cannot be used. To import the module into your Python script, the module must be in an enclosing directory, for example, as a submodule of your project. Then, you can import it relative to your script. For example, if your repository has the following structure, then inside of *my_script.py*, you can import all relevant methods from this module with the line `from libs.stb_dxt import *`.

```
my_repo
  |_ my_script.py
  |_ libs
    |_ stb_dxt (submodule)
```

## Building

This module comes with prebuilt libraries for the following systems:

- Linux (Ubuntu 18.04) 64-bit (possibly 32-bit?)
- Windows (10) 32-bit or 64-bit

If you would like to re-build the libraries, follow these platform-specific instructions and remember to place libraries in their platform-specific folder in the *libs* directory.

*Linux*

Run the following command in terminal:

```bash
cc -fPIC -shared -o libs/lib_stb_dxt.so src/stb_dxt.c
```

*Windows*

Open the *Developer Command Prompt for VS 2019*. You can search for this in the start menu.  *Note: you must have Visual Studio 2019 installed.* Then, run this command:

```bash
cl /LD src\stb_dxt.c /Fo:"libs\windows\stb_dxt" /Fe:"libs\windows\stb_dxt"
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

See the example *example.py* for a complete example. It will take as input the image *example_assets/dog.jpg* and output the dxt file *example_assets/dog.dxt*. Included for reference/comparison is the file *example_assets/dog_reference.dxt*. You can run this example by using the command (e.g. with Python 2.7 on Windows):

```bash
python2 C:\path_to_stb_dxt\example.py
```

However, if python is not installed on your path, then you will need to explicitly call the python exe like this:

```bash
C:\Python27\python.exe C:\path_to_stb_dxt\example.py
```