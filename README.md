# Palm Tree Detection and Counting

## Project Overview

This project focuses on detecting and counting palm trees in images using deep learning techniques. It leverages a pre-trained model, `fasterrcnn_resnet50_fpn`, and fine-tunes it on a custom dataset with annotations provided in a CSV file format. The project also incorporates MLOps practices, including model versioning, data tracking, and performance monitoring, using tools like Docker and MLflow.

## Table of Contents
1. [Project Overview](#project-overview)

## Features

- **Object Detection**: Detects and counts palm trees in images using a fine-tuned Faster R-CNN model.
- **Model Performance Metrics**: Calculates Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to evaluate counting accuracy.
- **Image Preprocessing**: Automatically resizes images to 512x512 and normalizes bounding box coordinates.
- **Visualization**: Displays annotated images with bounding boxes and class labels.
- **API Integration**: Serves the model via a FastAPI application.
- **MLOps Integration**: Uses Docker for containerization and MLflow for experiment tracking and model management.
