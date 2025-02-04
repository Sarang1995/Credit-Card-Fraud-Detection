import streamlit as st

st.link_button("View Jupyter Notebook", "https://github.com/Sarang1995/Credit-Card-Fraud-Detection/blob/master/Credit%20Card%20Fraud%20Detection.ipynb")

st.title("Credit Card Fraud Detection using Machine Learning")

st.header("Objective")
st.write("The primary goal of this project is to develop a predictive classification model to detect **fraudulent transactions** in credit card payments. Since fraud detection is a high-risk problem where **False Negatives** (missed fraud cases) can lead to severe financial loss, the focus is on maximizing the **recall score** to correctly identify fraudulent transactions.")

st.header("Data Exploration & Challenges")
st.write("The dataset used for this project was **highly imbalanced**, with fraudulent transactions being a small fraction of total transactions. This posed a major challenge because traditional machine learning models tend to favor the majority class, leading to poor fraud detection.")
st.write("To address this, multiple **data balancing techniques** were used:")
st.write("""
         1. **Changing the threshold value** to optimize recall.
         2. **Undersampling** (reducing majority class samples). 
         3. **Oversampling** (duplicating minority class samples).
         4. **SMOTE (Synthetic Minority Over-sampling Technique)** to generate synthetic fraud samples.
         5. **Modifying the class_weight parameter** in models to penalize misclassification of fraud cases.
         """)

st.header("Model Selection & Training")
st.write("multiple machine learning models were trained using each of the **imbalance handling techniques** mentioned above:")
st.write("""
         1. Logistic Regression
         2. Decision Tree
         3. Random Forest
         4. KNN
         5. Gredient Boosting
         6. AdaBoost
         """)
st.write("Each model was evaluated based on performance metrics such as **accuracy**, **precision**, **recall** and **F1-score**.")

st.header("Best Performing Model & Results")

st.write("Among all the models and techniques, the **Random Forest classifier** with **class_weight adjustment** and **threshold tuning** provided the best results. This model effectively handled the imbalance in the dataset while maximizing **recall**, ensuring that fraudulent transactions were detected with higher sensitivity.")
st.write("Since the primary goal was reducing **False Negatives** (missed fraud cases), **recall score** was the key metric for evaluation. The best-performing model achieved:")

st.image("scores.png")

st.subheader("Confusion Matrix")
st.image("Confusion_matrix.png")

st.link_button("View Jupyter Notebook", "https://github.com/Sarang1995/Credit-Card-Fraud-Detection/blob/master/Credit%20Card%20Fraud%20Detection.ipynb")