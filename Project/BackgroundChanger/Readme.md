# SelfiSegmentation Application with OpenCV and cvzone

This Python script demonstrates real-time background removal using the SelfiSegmentation module from cvzone library in combination with OpenCV. It allows you to replace the background of the webcam feed with images from a directory.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- cvzone library (`cvzone`)
  - Install using: `pip install cvzone`

## Installation

1. Clone the repository or download the script.
2. Install the required libraries mentioned above.
3. Prepare a directory with images (`imglist`) to be used as backgrounds. Update the script with the correct path (`C:\\Users\\TANISHQ\\WALLPAPERS` in this case) where images are stored.

## Usage

1. Run the script. It will initialize the webcam and load the first image from the specified directory.
2. Use the following keys to interact with the application:
   - `a`: Move to the next background image in the directory.
   - `d`: Move to the previous background image in the directory.
   - `q`: Quit the application.
   
3. The script will continuously update the background of the webcam feed based on the selected image.

## Script Overview

- The script uses `cv2.VideoCapture` to capture video from the webcam.
- It loads images from a specified directory and allows cycling through them using keyboard inputs (`a` and `d`).
- `SelfiSegmentation` from cvzone is used to perform real-time background removal.
- The `FPS` module from cvzone is used to display the frames per second (FPS) on the output window.
- Press `q` to quit the application.

## Folder Structure

Ensure the folder structure and paths are correctly set up as per your system configuration. Modify paths in the script (`imglist` and background image directory) if necessary.

## Notes

- This script demonstrates a basic implementation of background removal. You can adjust parameters (`cutThreshold`) in `SelfiSegmentation` for better results depending on lighting conditions and image backgrounds.

Feel free to modify and expand upon this script according to your project requirements or explore additional functionalities provided by the `cvzone` library.

