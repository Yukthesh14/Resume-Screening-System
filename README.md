#  Resume Screening System

A machine learning-based resume screening application that analyzes uploaded PDF resumes and classifies them into **Shortlist** or **Review** categories.

The application uses a trained text-classification pipeline and provides the prediction along with model probability estimates through an interactive Streamlit interface.

##  Live Demo

**[Try the Resume Screening System](https://resume-screening-system-e6upxnzhsja3dbzuntgud2.streamlit.app/)**

##  Source Code

**[GitHub Repository](https://github.com/Yukthesh14/Resume-Screening-System/blob/main/model_training.ipynb)**

---

##  Project Overview

Recruitment teams may need to review a large number of resumes during an initial screening process. This project demonstrates how machine learning can be used to automate a basic first-level resume classification task.

The system accepts a PDF resume, extracts its text, processes the text using the trained machine learning pipeline, and returns one of two classifications:

- **Shortlist**
- **Review**

The application also displays the model's estimated probability for each class and flags predictions below the configured confidence threshold for additional human review.

---

##  Objectives

- Build a text-classification model for resume screening.
- Convert resume text into numerical features using TF-IDF.
- Compare machine learning classification approaches.
- Evaluate the selected model on a held-out test set.
- Save the complete trained ML pipeline.
- Build an interactive Streamlit application.
- Enable PDF resume upload and automatic text extraction.
- Deploy the application using Streamlit Community Cloud.

---

##  Machine Learning Workflow

```text
Resume Dataset
      ↓
Data Preparation
      ↓
Train / Test Split
      ↓
TF-IDF Vectorization
      ↓
Model Training
      ↓
Cross-Validation
      ↓
Best Model Selection
      ↓
Final Test Evaluation
      ↓
Save Trained Pipeline
      ↓
Streamlit Application
