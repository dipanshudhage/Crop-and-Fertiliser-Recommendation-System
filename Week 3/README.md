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
1. **Clone the repository**:
    ```bash
    git clone https://github.com/dipanshudhage/Crop-and-Fertiliser-Recommendation-System.git
    ```

2. **Install required dependencies**:
    Navigate to the project directory and install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    Start the Streamlit web application:
    ```bash
    streamlit run app.py
    ```

4. **Upload soil test reports**:
    You can upload images or PDFs of soil test reports, and the system will provide crop and fertilizer recommendations.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **scikit-learn**: For machine learning model building.
- **Streamlit**: For creating an interactive web interface.
- **Pytesseract & PyMuPDF**: For extracting text from image and PDF files.

---

Feel free to make adjustments based on your preferences! This README file provides a clear understanding of the project and guides users on how to set it up. Would you like help with anything else?
