# predictive-maintenance-system

 A Machine Learning based predictive maintanance system  thsat analyzing industrial machine sensor data and predicts 
 potential machine failures using a Random Forest Classifier.

 Project Overview

This project aims to idenfity potential machine failures before they occur by analyzing industrial sensor measurements.
The system uses machine learning techniques to evalute sesnor data estimate faiulure risk and provide predictions throug an interactive web application.
The project combines data analysis, machine learning, model evalution, and application devolopment.

Objectives

-Analyze industral machine sensor data.
-Idenfity pstterns associated with machine failures.
-Devolop a predictive machine learning model.
-Evaluete model performance using classification metrics.
-Provide an interactive interface for real time predictions

Technologies Used

-Python
-Pandas
-NumPy
-Matlotlib
-Seaborn
-Scikit-learn
-Random Forest Classifier
-Streamlit
-Joblib

Dataset
The project uses industrial machine sensor data to devolop and evaluete a predictive maintanence model.

The dataset inculudes 10.000 record containing machine oparating conditions end sensor measurement, inculuding:
-Air Temparature (K)
-Process Temperature(K)
-Rational Speed(rpm)
-Torgue(Nm)
-Tool Wear(min)
-Machine Type

The target veriable is machine faiulure which indicates whether a machine faiulure occurred.

Dataset Source: UCI Machine Learning Repository AI 2020 Predective Maintenance Dataset.


Methodology
1.Explory Data Analysis
-Dataset inspection
-Statiscal analysis
-Missing value analysis
-Faiulure distribution analysis
-Correlation analysis
-Feature visualaziton

2.Data Proprecessing
-Removal of irrelevant identifiers
-Prevention of target leakage
-Cotogarical feature encoding 
-Feature and target separation
-Stratified train test split

3.Model Devolopment
A Random Forest Classifier was trained to predict machine failures.

-100 estimators 
-Balenced class weights
-%80 training data
-%20 testing data

4.Model Devolopment
The model evalueted using:
-Accurary
-Precision
-Recall
-F1-Score
-Confision Matrix 
-ROC-AUC
-Precision-Recall Curve
-Cross-Validation

Additional thresold optimization was performed to improve faiulure detection.

5.Interactive Prediction Application
A Streamlit application was devoloped to allow users to enter machine sensor measurements and receive faiulure risk predictions.

Features include:
-Machine type selection
-Sensor value inputs
-Failure risk estimaton
-Low Risk/High Risk classification
-Interactive prediction interface

Model Performance

Evalution Metric                           Result
Accurary (default threshold)               %98.1
ROC-AUC                                    0.9632
Avarege Precision                          0.7955
Cross-Validation Mean F1                   0.5999

A decision threshold of 0.30 was also tested to improve faiulure detection reccall.


Application
The application provides an interactive interface for entering sensor measurements and predicting potential machine failures.
The trained model is saved in .pk1 format and loaded by the streamlit application.

Project Structure
predictive-maintenance-system/
       predictive-maintanece-system.ipynb
       app.py
       requirements.txt
       predictive-maintenance_model.pk1
       README.md
       screenshots/


Installation and Usage
Clone the repository
Bash
git clone https://github.comelifleyla12ozlem-pixel

Nevigate to the project directory
Bash
cd predictive-maintenance-system

Install dependencies
Bash
pip install-r requirements.txt

Run the application
Bash
streamlit run app.py


Testing
The application was tested using different machine sensor confiqurations.

Two tested scenarios were evaluted:
-Normal operating conditions
-Increased torque and tool wear conditions

The application succesfully generated different faiulure risk predictionsfor the tested scenarius.

Author 
Elif Özdilek

Mechatronics Technician Machine Learning Python Data Analythics
GitHub: elifleya12ozlem-pixel

This project was devoloped for educational and portfolio purposes. Model predictions are not a substitute for industral safety 
system or proffesional maintenance inspections.



