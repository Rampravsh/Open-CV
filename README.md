# OpenCV Learning Repository

This repository contains a collection of Python scripts demonstrating various functionalities of the OpenCV library. It's designed for learning and practicing computer vision concepts.

## Table of Contents

*   [Prerequisites](#prerequisites)
*   [Usage](#usage)
*   [Scripts Overview](#scripts-overview)
    *   [1. Basic Image Operations](#1-basic-image-operations)
    *   [2. Image Drawing](#2-image-drawing)
    *   [3. Image Resizing & Shaping](#3-image-resizing--shaping)
    *   [4. Filtering & Blurring](#4-filtering--blurring)
    *   [5. Contour & Shape Detection](#5-contour--shape-detection)
    *   [6. Face Detection](#6-face-detection)
    *   [7. Video Functions](#7-video-functions)
    *   [8. Projects](#8-projects)
*   [Upcoming Plan](#upcoming-plan)

## Prerequisites

Before running any of the scripts, you need to have Python and the following libraries installed:

*   **OpenCV:** `pip install opencv-python`
*   **NumPy:** `pip install numpy`

## Usage

Most scripts can be run directly from the command line:

```bash
python <directory_name>/<script_name>.py
```

For example:

```bash
python "image Resizing & Shaping"/resize.py
```

## Scripts Overview

### 1. Basic Image Operations

*   `read_image.py`: Demonstrates how to read and display an image.
*   `grayscale.py`: Converts an image to grayscale.
*   `dimensions.py`: Gets the dimensions of an image.
*   `saving.py`: Shows how to save an image to a file.
*   `imagedraw.py`: A general script for drawing on images.

### 2. Image Drawing

Located in the `image drawing function/` directory.

*   `draw_line.py`: Draws a line on an image.
*   `draw_rectangle.py`: Draws a rectangle on an image.
*   `draw_circle.py`: Draws a circle on an image.
*   `draw_text.py`: Writes text on an image.

### 3. Image Resizing & Shaping

Located in the `image Resizing & Shaping/` directory.

*   `resize.py`: Resizes an image to a specific dimension.
*   `cropped.py`: Crops a region of interest from an image.
*   `rotation.py`: Rotates an image.
*   `flipped.py`: Flips an image horizontally, vertically, or both.

### 4. Filtering & Blurring

Located in the `filtering & Blurring/` directory.

*   `gaussian_blur.py`: Applies Gaussian blur to an image.
*   `median_blur.py`: Applies median blur to an image.

### 5. Contour & Shape Detection

Located in the `contour & Shape Detection/` directory.

*   `contour_fun.py`: Finds and draws contours in an image.

### 6. Face Detection

*   `face_detection.py`: Performs basic face detection using a Haar cascade classifier.

### 7. Video Functions

Located in the `video function/` directory.

*   `using_cap.py`: Captures video from a webcam.
*   `saving_video.py`: Captures video from a webcam and saves it to a file.

### 8. Projects

*   `project 1/project1.py`: Project 1 description.
*   `project 2/project2.py`: Project 2 description.

## Upcoming Plan

Here are some ideas for future additions to this repository:

*   **Object Tracking:** Implement object tracking algorithms like KCF, CSRT, or MOSSE.
*   **Advanced Image Thresholding:** Explore different thresholding techniques.
*   **Color Spaces:** Work with different color spaces like HSV and LAB.
*   **More Projects:** Add more complex projects combining multiple OpenCV concepts.
*   **Deep Learning Integration:** Integrate deep learning models for tasks like object detection (e.g., using YOLO) or image classification.
