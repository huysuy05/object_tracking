# Object Detection and Tracking System

This script demonstrates an object detection and tracking system using TensorFlow and OpenCV. It detects objects within video frames, identifies their centers, and tracks their positions across consecutive frames using Euclidean distance.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Code Walkthrough](#code-walkthrough)
   - [Object Detection](#object-detection)
   - [Tracking Mechanism](#tracking-mechanism)
   - [Displaying Results](#displaying-results)
4. [Concepts](#concepts)
   - [Center Point Calculation](#center-point-calculation)
   - [Euclidean Distance](#euclidean-distance)
   - [Object ID Tracking](#object-id-tracking)

---

## Overview

This project reads a video file ('cars.mp4'), detects objects within each frame, and tracks their movement across frames. By maintaining a unique ID for each object, it achieves continuous tracking, even if objects temporarily leave the frame.

## Getting Started

To run this code, make sure you have OpenCV and TensorFlow installed:

\`\`\`bash
pip install opencv-python-headless tensorflow
\`\`\`

## Code Walkthrough

### Object Detection

The \`ObjectDetection\` class is initialized to detect objects in each frame. Each object's bounding box is extracted, and its center point is calculated.

### Tracking Mechanism

Object tracking across frames is achieved by:
1. Calculating the Euclidean distance between objects in the current and previous frames.
2. Assigning a unique ID to each detected object if it does not already exist.

### Displaying Results

Each frame is displayed with bounding boxes around detected objects, circles at the center points, and labels showing object IDs. The display updates in real-time as the video plays.

## Concepts

### Center Point Calculation

The center point for each detected bounding box is calculated by averaging its x and y coordinates. This point serves as the basis for tracking objects across frames.

### Euclidean Distance

The Euclidean distance between center points in consecutive frames is used to determine if a detected object in the current frame matches an object from the previous frame.

### Object ID Tracking

Each object receives a unique ID, which persists as long as it remains within a threshold distance across frames. If an object exits the frame or its ID is not matched, it is removed from the tracking list.

---

This README provides a structured overview of an object detection and tracking system, covering initialization, detection, tracking, and display processes. This code demonstrates foundational principles for real-time object tracking in video.
