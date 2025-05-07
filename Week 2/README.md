
# 🌾 Crop and Fertiliser Recommendation System using Machine Learning

This project is part of the **AICTE SKILL4FUTURE – Week 2** challenge. It provides a machine learning-based solution to help farmers make informed decisions on which **crop to grow** and which **fertiliser to use** based on soil nutrients and environmental conditions.

---

## 🎯 Problem Statement

Many Indian farmers face challenges in selecting suitable crops and fertilizers due to a lack of scientific guidance. This results in low productivity and soil degradation.

---

## 💡 Proposed Solution

This project uses supervised machine learning to:
- Recommend the **most suitable crop** based on soil and climate data.
- Suggest the **best fertilizer** based on the crop, soil type, and nutrient levels.

All implementation is done in a **Google Colab notebook**, making it easy to run without any local setup.

---

## 📁 Project Files

| File Name                  | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `Crop Prediction.ipynb`   | Google Colab notebook for model building and prediction      |
| `Crop_recommendation.csv` | Dataset for crop prediction based on NPK and climate data    |
| `Fertilizer Prediction.csv` | Dataset for fertilizer prediction based on soil and crop info |

---

## 📊 Dataset Overview

### 1. Crop Recommendation
- **Features**: Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall  
- **Target**: Crop Label (e.g., rice, wheat, cotton)

### 2. Fertilizer Recommendation
- **Features**: Soil Type, Crop Type, Temperature, Humidity, Moisture, Nitrogen, Phosphorus, Potassium  
- **Target**: Fertilizer Name (e.g., Urea, DAP, 28-28)

---

## 🧠 Machine Learning Workflow

- Data preprocessing and cleaning  
- Label encoding for categorical values  
- Model training using classification algorithms (e.g., Random Forest)  
- Evaluation and testing on sample inputs

---

## 🛠️ Technologies Used

- **Google Colab**  
- **Python**  
- **Pandas**, **NumPy**, **Scikit-learn**  
- Jupyter Notebook environment (via Colab)

---

## 🚀 Output

- Recommends a crop based on user-inputted soil and climate conditions  
- Suggests the best fertilizer based on selected crop and soil nutrient levels

---

## 🔮 Future Scope

- Deploy the model in a **Streamlit web app** for easier use by farmers  
- Integrate **speech input/output** for regional language support  
- Connect with **real-time weather data APIs** for dynamic predictions

---

## 👨‍💻 Contributor

- **[Your Name]**  
- Submitted under **AICTE SKILL4FUTURE Program – Week 2**
