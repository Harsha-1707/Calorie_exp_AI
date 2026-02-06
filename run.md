# Running the Calorie Prediction Project

This guide will help you set up and run the Calorie Prediction web application on your local machine.

## Prerequisites

- **Python 3.8+** installed.
- **pip** (Python package installer).

## 1. Install Dependencies

First, ensure you have the required libraries installed. Run the following command in your terminal:

```bash
pip install pandas xgboost scikit-learn flask
```

## 2. Train the Model

Before running the application, you must train the XGBoost model. This step processes the data and saves the model as `model.pkl`.

```bash
python train_model.py
```

_Expected Output:_

```
Loading data...
Merging datasets...
Preprocessing...
...
Model MAE: 1.49...
Saving model to model.pkl...
Done!
```

## 3. Run the Application

Start the Flask web server:

```bash
python app.py
```

_Expected Output:_

```
 * Running on http://127.0.0.1:5000
```

## 4. Access the App

Open your web browser and navigate to:
**[http://localhost:5000](http://localhost:5000)**

You should see the "Calorie Cruncher" interface. Enter the required details and click "Calculate Calories" to get your prediction.
