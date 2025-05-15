# AI-Powered Crop and Fertilizer Recommendation System

## Overview
This project provides an AI-powered recommendation system designed to assist farmers in selecting the most suitable crop and fertilizer based on soil health data. By analyzing soil test reports (either from images or PDFs), the system generates tailored recommendations to help farmers optimize their agricultural practices and improve productivity.

## Features
- **Upload Soil Test Report**: Users can upload images or PDF files of soil test reports.
- **Crop and Fertilizer Recommendation**: Based on the soil test data, the system recommends the best crops and fertilizers.
- **User-Friendly Interface**: Built with Streamlit to provide an interactive and easy-to-use web interface.
- **AI Model**: Utilizes machine learning models trained on historical data to make accurate recommendations.

## Technologies Used
- **Python**: The programming language used for development.
- **Streamlit**: Framework used to create the web interface.
- **scikit-learn**: Machine learning library used for training models (RandomForestClassifier).
- **Pytesseract**: OCR tool used to extract text from soil test report images.
- **PyMuPDF (fitz)**: Used to extract text from PDF files.

## Project Structure
The project contains the following important files and folders:
- **app.py**: Main Streamlit application file.
- **models/**: Folder containing trained models for crop and fertilizer prediction (`model_crop.pkl`, `model_fertilizer.pkl`).
- **data/**: Folder containing datasets used for training the models.
- **assets/**: Folder containing any images or resources used for the project.
- **ppt/**: Folder containing the PowerPoint presentation for the project.

## Datasets
- **Crop Recommendation Dataset**: Includes information about different crops and their recommended soil nutrient levels (N, P, K, etc.).
- **Fertilizer Dataset**: Contains various fertilizers and their corresponding nitrogen, phosphorus, and potassium content.

## How to Run the Project
# 🌾 Crop and Fertilizer Recommendation System using Machine Learning

This project is an AI-powered system designed to recommend the most suitable crops and fertilizers based on soil nutrient levels and environmental conditions. It uses machine learning models trained on real agricultural datasets and allows users to input data manually or extract it from soil report PDFs/images.

---

## 🚀 Open in Google Colab

<a href="https://colab.research.google.com/github/dipanshudhage/Skill4Future/blob/main/Week%203/Crop%20and%20Fertiliser%20Recommendation%20System/App/app.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

---

## 📌 Features

- Upload soil test reports in **image or PDF format**.
- Automatically extracts N, P, K values using OCR.
- Recommends the best **crop** and **fertilizer** based on input.
- Built using **Streamlit**, **scikit-learn**, and **OCR tools**.

---

## 🧠 How to Run the Project (Google Colab)

1. Open the notebook using the **"Open in Colab"** button above.

2. **Upload all required model files when prompted**:
   - `model_crop.pkl`
   - `label_encoder_crop.pkl`
   - `model_fertilizer.pkl`
   - `label_encoder_fertilizer.pkl`

   ⚠️ **Warning:** You must upload **all four `.pkl` files** before running the prediction cells.

3. Enter the soil and environmental values when prompted.

4. The system will output:
   - ✅ **Recommended Crop**
   - ✅ **Recommended Fertilizer**

---

## 🛠️ Technologies Used

- **Python**, **scikit-learn**, **pandas**
- **Tesseract OCR**, **PyMuPDF**
- **Google Colab** for runtime
- **Pre-trained ML models** for prediction

---
## 💻 How to Run the Project (Streamlit Version - Local)

You can also run the project locally on your computer using **Streamlit**. Follow these steps:

### 📥 Step 1: Download Files

Download the following files into the **same folder**:
- `app.py`
- Model files:
  - `model_crop.pkl`
  - `label_encoder_crop.pkl`
  - `model_fertilizer.pkl`
  - `label_encoder_fertilizer.pkl`
- `requirements.txt`

> You can get them from the [GitHub repository](https://github.com/dipanshudhage/Skill4Future).

---

### ⚙️ Step 2: Install Python and Required Libraries

1. Make sure **Python 3.8+** is installed.  
   Download: [https://www.python.org/downloads](https://www.python.org/downloads)

2. Open **Command Prompt** (or Terminal), navigate to your project folder, and run:

```bash
pip install -r requirements.txt
```
## ❗ If requirements.txt gives an error, install libraries manually:
```bash
pip install streamlit==1.15.0
pip install pandas==1.4.2
pip install scikit-learn==1.0.2
pip install pytesseract==0.3.8
pip install Pillow==8.4.0
pip install PyMuPDF==1.19.4
pip install joblib==1.1.0

```
##🚀 Step 3: Run the App
Run the Streamlit application:
```bash
streamlit run app.py
```
It will open in your default browser. Upload a soil report and input values to get crop and fertilizer recommendations.

## ⚠️ Important:
Make sure all .pkl model files are present in the same folder as app.py. Missing any of them will cause the app to fail.

## 📌 Features
Upload soil test reports in image or PDF format.
Automatically extracts N, P, K values using OCR.
Recommends the best crop and fertilizer based on input.
Built using Streamlit, scikit-learn, and OCR tools.

## 🛠️ Technologies Used
Python, scikit-learn, pandas
Tesseract OCR, PyMuPDF
Streamlit and Google Colab
Pre-trained ML models for prediction

## License
This project is licensed under the MIT License.

## Acknowledgments
- **scikit-learn**: For machine learning model building.
- **Streamlit**: For creating an interactive web interface.
- **Pytesseract & PyMuPDF**: For extracting text from image and PDF files.
