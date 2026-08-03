# Comparative Evaluation of CNN Models for Sri Lankan Chilli Leaf Disease Detection

## IT41043 – Intelligent Systems
### Milestone 2 – Methodology and Data Description

## Project Overview

This project was developed for the Intelligent Systems (IT41043) module at Horizon Campus.

The main objective of this research is to compare the performance of three Convolutional Neural Network (CNN) models for detecting chilli leaf diseases using images collected from Sri Lankan farms. The selected CNN models are MobileNetV2, ResNet50 and EfficientNetB0.

Unlike many previous studies that use benchmark datasets collected under laboratory conditions, this research focuses on locally collected chilli leaf images captured under real farming conditions. The comparison will help identify the most suitable CNN architecture for disease detection in Sri Lankan agriculture.

---

# Research Objectives

- Collect chilli leaf images from Sri Lankan farms.
- Build a locally collected image dataset.
- Preprocess the collected images for model training.
- Compare the performance of MobileNetV2, ResNet50 and EfficientNetB0.
- Evaluate each model using the same dataset and training conditions.
- Identify the most suitable CNN model for chilli leaf disease detection.

---

# Selected CNN Models

- MobileNetV2
- ResNet50
- EfficientNetB0

---

# Dataset

The dataset consists of chilli leaf images collected from Sri Lankan agricultural fields.

Expected disease classes include:

- Healthy Leaves
- Bacterial Leaf Spot
- Leaf Curl Disease
- Anthracnose / Other Common Diseases

The images will be resized, normalized and augmented before model training.

---

# Data Preprocessing

The preprocessing stage includes:

- Removing duplicate images
- Image resizing (224 × 224 pixels)
- Image normalization
- Data augmentation
  - Rotation
  - Horizontal Flip
  - Zoom
  - Brightness Adjustment
- Dataset splitting (Training, Validation and Testing)

---

# Evaluation Metrics

The CNN models will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Validation Loss
- Training Time

The research will use Stratified 5-Fold Cross Validation to ensure a fair comparison between models.

---

# Project Structure

```
srilankan-chilli-leaf-disease-cnn/
│
├── dataset/
│
├── preprocessing/
│   ├── data_cleaning.py
│   ├── resize_images.py
│   └── augmentation.py
│
├── models/
│   ├── mobilenetv2.py
│   ├── resnet50.py
│   └── efficientnetb0.py
│
├── evaluation/
│   ├── metrics.py
│   ├── confusion_matrix.py
│   └── comparison.py
│
├── results/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Software and Tools

- Python 3.x
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Git
- GitHub

---

# Current Project Status

✅ Research topic selected

✅ Literature review completed

✅ Methodology completed

✅ Dataset planning completed

✅ GitHub repository created

✅ Project folder structure prepared

✅ Preprocessing scripts added

⬜ Dataset collection in progress

⬜ Model training

⬜ Performance evaluation

⬜ Final comparison

---

# Repository

GitHub Repository

https://github.com/Dilani410/srilankan-chilli-leaf-disease-cnn

---

# Project Members

| Name | Student ID |
|------|------------|
| A.W.Dilani Ayesha | (ITBIN-2313-0047) |
| W. Elika Sevindya | (ITBIN-2313-0119) |

---

# Module Information

Module Code: IT41043

Module: Intelligent Systems

Assignment: Milestone 2 – Methodology and Data Description

Faculty: Faculty of Information Technology

Institution: Horizon Campus

Academic Year: 2026

---

# Supervisor

Mr. Isuru Madusanka Samarappulige

Faculty of Information Technology

Horizon Campus

---

## License

This repository is created for academic purposes as part of the IT41043 Intelligent Systems module at Horizon Campus.
