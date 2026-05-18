# Titanic Survival Prediction 🚢📊

## Overview
The Titanic dataset is one of the most famous datasets used for Data Science and Machine Learning practice. It is based on the tragic sinking of the RMS Titanic on April 15, 1912, after hitting an iceberg during its maiden voyage from Southampton to New York City. Out of more than 2,200 passengers and crew members, over 1,500 lost their lives.

This project focuses on analyzing passenger information and building a Machine Learning model to predict whether a passenger survived the disaster.

## About the Dataset
The dataset contains information about Titanic passengers, including personal details and travel information.

### Features in the Dataset

1. `PassengerId` – Unique ID for each passenger  
2. `Survived` – Survival status (0 = No, 1 = Yes)  
3. `Pclass` – Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)  
4. `Name` – Passenger name  
5. `Sex` – Gender  
6. `Age` – Age in years  
7. `SibSp` – Number of siblings/spouses aboard  
8. `Parch` – Number of parents/children aboard  
9. `Ticket` – Ticket number  
10. `Fare` – Fare paid  
11. `Cabin` – Cabin number  
12. `Embarked` – Port of embarkation  
   - C = Cherbourg  
   - Q = Queenstown  
   - S = Southampton  

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

## Libraries Used

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```

## Data Preprocessing
Some columns in the dataset contained missing values.

- The `Cabin` column had too many missing values, so it was removed.
- Missing values in the `Age` column were filled using the average age.
- Missing values in the `Embarked` column were filled using the most common value.
- Unnecessary columns such as `Name` and `Ticket` were removed.
- Categorical columns like `Sex` and `Embarked` were converted into numerical values using encoding techniques.

## Exploratory Data Analysis (EDA)

### Correlation Analysis

1. **Pclass and Fare**
   - Negative correlation
   - Passengers in 1st class paid higher fares, while 3rd class passengers paid lower fares.

2. **Fare and Survived**
   - Positive correlation
   - Passengers who paid higher fares had better chances of survival.

3. **Pclass and Survived**
   - Negative correlation
   - Lower-class passengers had lower survival rates.

4. **SibSp and Parch**
   - Positive correlation
   - Families often traveled together.

5. **Age and Survived**
   - Weak correlation
   - Age did not strongly affect survival chances.

6. **Fare and Parch / SibSp**
   - Slight positive correlation
   - Families or groups may have booked tickets together.

### Survival Analysis
The count plot of the `Survived` column showed that more passengers did not survive the disaster compared to those who survived. The bar representing non-survivors was much taller, indicating the severity of the tragedy and the overall low survival rate.

## Workflow
1. Data Collection
2. Data Cleaning
3. Handling Missing Values
4. Exploratory Data Analysis
5. Feature Engineering
6. Data Preprocessing
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Prediction System

## Model Performance
The Titanic Survival Prediction project successfully predicted passenger survival using Machine Learning techniques.

- Training Accuracy: 80%
- Testing Accuracy: 78%

The model performed well and produced reliable predictions based on passenger information.

## Key Insights
- Female passengers had higher survival chances.
- Passengers traveling in 1st class had better survival rates.
- Higher fare-paying passengers were more likely to survive.
- Family relationships influenced travel patterns and survival.

## Conclusion
This project demonstrates how Machine Learning can be applied to real-world historical datasets to identify survival patterns and make predictions. Through preprocessing, visualization, and predictive modeling, the project achieved good accuracy and meaningful insights into the Titanic disaster.

## Author
Agi Ann Maria