import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pickle
import os

def train():
    print("Loading data...")
    calories = pd.read_csv('calories.csv')
    exercise = pd.read_csv('exercise.csv')

    print("Merging datasets...")
    data = pd.merge(exercise, calories, on='User_ID')

    print("Preprocessing...")
    # Gender encoding: male -> 0, female -> 1
    data.replace({"Gender": {'male': 0, 'female': 1}}, inplace=True)

    X = data.drop(columns=['User_ID', 'Calories'])
    y = data['Calories']

    print(f"Features: {X.columns.tolist()}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training XGBoost model...")
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model MAE: {mae}")

    print("Saving model to model.pkl...")
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Done!")

if __name__ == "__main__":
    train()
