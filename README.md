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

## 🧠 Machine Learning Workflow

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

---

## 🛠️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Multinomial Naive Bayes
- Cross-Validation

### Data Processing

- Pandas
- NumPy

### PDF Processing

- PyPDF

### Application & Deployment

- Streamlit
- Joblib
- Git
- GitHub
- Streamlit Community Cloud

---

## 🤖 Model Development

Two machine learning approaches were evaluated for resume text classification:

- Multinomial Naive Bayes
- Logistic Regression

The models were evaluated using stratified cross-validation on the training data.

The best-performing model was selected and then retrained on the complete training set before final evaluation on the held-out test set.

The final trained pipeline was saved as:

`resume_classifier.pkl`

---

## 📊 Model Evaluation

The selected model was evaluated on a held-out test set using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Test Result

- Test samples: 25
- Correct predictions: 25
- Incorrect predictions: 0
- Accuracy: 100%
- Macro F1-score: 1.00

These results are specific to the current manually constructed dataset and test split. They should not be interpreted as production-level hiring accuracy.

---

## 💻 Application Features

- Upload PDF resumes through the Streamlit interface.
- Extract resume text automatically.
- Classify resumes as **Shortlist** or **Review**.
- Display Shortlist and Review probability estimates.
- Display model confidence.
- Flag low-confidence predictions for additional human review.
- Provide an interactive browser-based interface.

---

## 🔄 Application Workflow

PDF Resume  
↓  
Text Extraction  
↓  
Saved ML Pipeline  
↓  
TF-IDF Transformation  
↓  
Classification  
↓  
Shortlist / Review  
↓  
Probability Estimates  
↓  
Low-Confidence Warning

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Yukthesh14/Resume-Screening-System.git
```

### 2. Navigate to the project directory

```bash
cd Resume-Screening-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

[Launch the Resume Screening System](https://resume-screening-system-e6upxnzhsja3dbzuntgud2.streamlit.app/)

---

## ⚠️ Limitations

- The current dataset is relatively small.
- The dataset is manually constructed for learning and demonstration.
- Resume wording can significantly influence predictions.
- The model may perform poorly on terminology that was not sufficiently represented in the training data.
- Model probability estimates should not be interpreted as guaranteed probabilities of correctness.
- The current system performs general resume classification rather than matching a resume against a specific job description.
- The confidence threshold used in the application is a prototype setting and has not been optimized using a large validation dataset.

---

## 🔐 Responsible Use

This application is intended as a **resume-screening decision-support system**, not as an autonomous hiring decision system.

For real-world recruitment use, additional validation would be required, including:

- Representative and sufficiently large training data
- Human oversight of model predictions
- Fairness and bias evaluation
- Privacy and data protection measures
- Monitoring of model performance after deployment

Users should avoid uploading confidential or sensitive candidate information to the public demonstration application.

---

## 🔮 Future Improvements

- Expand the training dataset with more representative resume examples.
- Introduce job-description-specific resume matching.
- Improve probability calibration.
- Optimize the confidence threshold using validation data.
- Add DOCX resume support.
- Add structured resume information extraction.
- Perform more systematic error analysis.
- Add model monitoring and performance tracking.
- Improve the user interface and reporting features.

---

## 👨‍💻 Author

**Motepalli Yukthesh**

---




