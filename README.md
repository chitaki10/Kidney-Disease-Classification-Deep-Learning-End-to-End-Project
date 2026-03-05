# Kidney Disease Classification – End-to-End Deep Learning Project

<div align="center">

## 🏥 AI-Powered Kidney Disease Detection  
### Production-Ready CNN + MLOps Pipeline 🚀  

</div>

---

## 📌 Project Overview

This project is a **complete end-to-end deep learning system** for classifying kidney CT/ultrasound images into:

- 🟢 Normal  
- 🟡 Cyst  
- 🔵 Stone  
- 🔴 Tumor  

It leverages **Transfer Learning (VGG16)** and follows **MLOps best practices** to ensure scalability, reproducibility, and production deployment.

This project demonstrates:

- ✅ Modular ML pipeline design  
- ✅ Experiment tracking with MLflow  
- ✅ Data versioning with DVC  
- ✅ Dockerized deployment  
- ✅ CI/CD ready infrastructure  
- ✅ Streamlit real-time inference  

---

## 🎯 Problem Statement

Early detection of kidney diseases using imaging can significantly improve treatment outcomes.  
This project builds a CNN-based classifier capable of predicting kidney conditions from CT/ultrasound scans.

---

## 🧠 Model Architecture

- Base Model: **VGG16 (Transfer Learning)**
- Framework: TensorFlow 2.x / Keras
- Image Size: 224x224
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Output: 4-class softmax classifier
- Fine-tuning enabled

---

## 📊 Performance Metrics

| Model | Train Accuracy | Validation Accuracy | F1-Score | ROC-AUC |
|-------|---------------|--------------------|----------|----------|
| VGG16 (Fine-tuned) | 90.07% | 71.81% | 0.72 | 0.89 |
| Custom CNN | 85.2% | 68.4% | 0.69 | 0.85 |

> Note: Validation gap suggests slight overfitting. Future improvements include augmentation and regularization tuning.

---

## 🛠️ Tech Stack

### 🔹 Machine Learning
- TensorFlow 2.x
- Keras
- VGG16
- NumPy
- Pandas

### 🔹 MLOps
- MLflow (Experiment Tracking)
- DVC (Data Version Control)
- Git
- Structured Logging
- Custom Exception Handling

### 🔹 API & UI
- Streamlit
- FastAPI (optional API layer)

### 🔹 Infrastructure
- Docker
- AWS EC2
- AWS S3
- GitHub Actions (CI/CD)

---

## 📂 Project Structure


├── app.py # Streamlit UI
├── src/
│ ├── config/ # YAML configuration files
│ ├── components/ # Data, Model, Evaluation modules
│ ├── pipeline/ # Training pipeline scripts
│ └── utils/ # Logging and exception handling
├── research/ # EDA notebooks
├── saved_models/ # Best trained model artifacts
├── MLflow_runs/ # MLflow experiment logs
├── dvc.yaml # DVC pipeline orchestration
├── requirements.txt # Dependencies
├── Dockerfile # Docker container setup
└── README.md


---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/chitaki10/Kidney-Disease-Classification-Deep-Learning-End-to-End-Project.git
cd Kidney-Disease-Classification-Deep-Learning-End-to-End-Project
