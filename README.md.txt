This is a Machine Learning web application built with Streamlit that predicts whether a person is likely to have Diabetes based on health data.

The model is trained using the Random Forest Classifier, which is an ensemble learning method that combines multiple decision trees to improve accuracy and reduce overfitting.

🚀 Features

User-friendly web interface (Streamlit).

Predicts diabetes risk using health attributes such as:

Pregnancies

Glucose Level

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

Deployed on Streamlit Cloud for easy access.

📊 Model Performance

Accuracy: 0.7402

Confusion Matrix:

[[83 17]
 [23 31]]


Classification Report:

               precision    recall  f1-score   support

           0       0.78      0.83      0.81       100
           1       0.65      0.57      0.61        54

    accuracy                           0.74       154
   macro avg       0.71      0.70      0.71       154
weighted avg       0.73      0.74      0.74       154

🛠️ Tech Stack

Python

Pandas, NumPy – Data processing

Scikit-learn – Random Forest model

Streamlit – Web app framework