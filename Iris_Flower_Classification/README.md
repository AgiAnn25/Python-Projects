# Iris Flower Classification 🌸📊

## Overview
The Iris Flower Dataset is one of the most well-known and beginner-friendly datasets in the field of Machine Learning and Data Analysis. Introduced by British biologist and statistician Ronald A. Fisher in 1936, this dataset is commonly used for classification and clustering problems. It helps in understanding the basic principles of pattern recognition and predictive modeling.

This project focuses on analyzing the Iris flower dataset and predicting the species of flowers using different Machine Learning algorithms.

## About the Dataset
The Iris dataset consists of 150 flower samples collected from three different species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

Each sample contains the following features:

- `SepalLengthCm` – Length of the sepal in centimeters
- `SepalWidthCm` – Width of the sepal in centimeters
- `PetalLengthCm` – Length of the petal in centimeters
- `PetalWidthCm` – Width of the petal in centimeters
- `Id` – Unique identifier for each flower sample

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Google Colab

## Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics

from sklearn.svm import SVC
from xgboost import XGBRegressor

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
```

## Exploratory Data Analysis (EDA)

The visualizations and analysis revealed several important insights:

- Iris-setosa has the smallest petal width with very low variation.
- Iris-virginica has the largest petal width values.
- There is clear separation between the flower species, making classification easier and more accurate.

## Workflow
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Prediction System

## Machine Learning Models Used
- Linear Regression
- Lasso Regression
- Ridge Regression
- Random Forest Regressor
- XGBoost Regressor
- Support Vector Classifier (SVC)

## Model Performance
Different machine learning models were tested to predict the species of Iris flowers based on their features.

- XGBoost Regressor gave the best performance with the lowest prediction error.
- Random Forest Regressor also performed very well and achieved results close to XGBoost.
- Linear Regression and Ridge Regression produced moderate results.
- Lasso Regression showed the weakest performance and was not suitable for this classification task.

Overall, XGBoost proved to be the most accurate and reliable model for predicting Iris flower species.

## Conclusion
This project demonstrates how Machine Learning algorithms can successfully classify flower species using simple numerical features. Through proper preprocessing, visualization, and model comparison, accurate predictions were achieved on the Iris flower dataset.

## Author
Agi Ann Maria