# Calorie Expenditure Modeling using XGBoost

## Overview

This project aims to model calorie expenditure using the XGBoost algorithm. The goal is to predict the number of calories burned during exercise based on various features such as user characteristics and exercise parameters. The dataset consists of two CSV files: `calories.csv`, containing user IDs and corresponding calorie counts, and `exercise.csv`, containing user information and exercise details.

## Files

1. **Xgboost_model.ipynb**: Jupyter Notebook containing the code for building and training the XGBoost model. This notebook includes data preprocessing, model training, evaluation, and prediction.

2. **calories.csv**: CSV file containing user IDs (`User_id`) and the corresponding calorie counts. Each row represents a record of calorie expenditure for a specific user.

3. **exercise.csv**: CSV file containing user information and exercise details. It includes columns such as `User_ID`, `Gender`, `Age`, `Height`, `Weight`, `Duration`, `Heart_Rate`, and `Body_Temp`. These features are used to predict calorie expenditure.

## Steps Involved

1. **Import Libraries:**
   - Necessary libraries like pandas, numpy, matplotlib, seaborn, and scikit-learn are imported.

2. **Load Datasets:**
   - The datasets are loaded from CSV files into pandas DataFrames.

3. **Merge Datasets:**
   - The datasets are merged on the `User_ID` column to create a consolidated dataset.

4. **Data Cleaning:**
   - Check for missing values and ensure there are no null entries.
   - Describe the dataset to get basic statistical insights.

5. **Data Visualization:**
   - Use seaborn to create count plots and distribution plots to visualize the data.
   - Create a heatmap to show the correlation between different features.

6. **Data Preprocessing:**
   - Convert categorical variables into numerical values (e.g., gender is converted to 0 for male and 1 for female).
   - Split the data into features (`x`) and target variable (`y`).

7. **Train-Test Split:**
   - Split the data into training and testing sets using `train_test_split` from scikit-learn.

8. **Model Training:**
   - Use `XGBRegressor` from the XGBoost library to train the model on the training data.

9. **Model Prediction and Evaluation:**
   - Make predictions on the test set.
   - Evaluate the model using Mean Absolute Error (MAE).

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Ananyaearth/TCR-Project-.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage Instructions

1. Ensure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost
   ```
2. Place the datasets (`calories.csv` and `exercise.csv`) in the specified directory or update the file paths accordingly.
3. Run the provided code in a Python environment (e.g., Jupyter Notebook, Spyder, or any other IDE).
4. The code will load the data, perform analysis, visualize the data, train an XGBoost regression model, and evaluate it using Mean Absolute Error.

## Note

- Ensure the file paths to the datasets are correct.
- The seaborn `distplot` function used in the code is deprecated; use `histplot` or `displot` instead for future compatibility.

---
