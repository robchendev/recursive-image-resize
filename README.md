# Bulk Image Resizer Script

This script is a Python script designed to automatically resize images in a specified directory to a user-defined maximum dimension for both width and height. The script also has an option to delete all non-image files within the directory, such as PSD files.

## Features

- **Uniform Resizing**: Resize all images to a specified maximum dimension for width and height.
- **Batch Processing**: Process all images in a designated directory at once.
- **Selective File Deletion**: Option to remove all non-image files from the directory after processing.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
- **Pillow Library**: This script uses the Pillow library for image processing, which can be installed using pip:

```bash
pip install Pillow
```

## Installation

1. Download the resizer.py script to your computer.
2. Place the script in the directory where you want to perform image resizing or ensure it is accessible from the command line.

## Usage

**IMPORTANT**: This will overwrite files within the directory, so it is important to make a backup of the directory before using the script in case the results are not as desired.

To use the Image Resizer Utility, open your command line interface (CLI) and navigate to the directory where resizer.py is located. Run the script using the following command format:

```bash
python resizer.py [max_dimension] [path_to_directory] [--delete]
```

[max_dimension]: The maximum size for both the width and height of the images in pixels.
[path_to_directory]: The path to the directory containing the images you wish to resize.
--delete (optional): Include this flag if you want to delete all non-image files in the directory after processing.

## Example Commands

Resizing Images: To recursively resize images in the /Users/Example/Pictures directory to a maximum dimension of 1024x1024 pixels:

```bash
python resizer.py 1024 /Users/Example/Pictures
```

To recursively resize images and delete all non-image files in the same directory:

```bash
python resizer.py --delete 1024 /Users/Example/Pictures
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
