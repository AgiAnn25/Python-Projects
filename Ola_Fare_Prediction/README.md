# Ola Ride Request Prediction 🚕📊

## Overview
The Ola Ride Request Prediction project aims to analyze and predict bike ride request demand using Machine Learning techniques. The dataset includes features related to ride requests, working hours, weather conditions, holidays, seasons, and yearly trends.

## Objective
The main objective of this project is to understand ride demand patterns and build predictive models that can estimate ride requests accurately based on different factors.

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
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics

from sklearn.svm import SVC
from xgboost import XGBRegressor

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
```

## Exploratory Data Analysis (EDA)

From the line plots, the following observations were identified:

1. There is no specific pattern in the day-wise average of ride requests.
2. More ride requests occur during working hours compared to non-working hours.
3. Ride requests dropped after the 7th month (July), likely due to festival holidays.

From the bar plots, the following observations were made:

- Ride request demand is high during summer and seasonal periods.
- Extreme weather conditions reduce bike ride demand because people prefer staying at home.
- Ride requests are lower on holidays because colleges and offices remain closed.
- Working hours show significantly higher ride requests than non-working hours.
- Bike ride requests increased significantly from the year 2011 to 2012.

## Workflow
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
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
- Support Vector Machine (SVM)

## Conclusion
This project demonstrates how Machine Learning can help analyze and predict ride demand patterns effectively. Factors such as working hours, weather conditions, seasonal changes, and holidays significantly influence ride requests.

## Author
Agi Ann Maria