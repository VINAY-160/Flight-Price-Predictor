# ✈️ Flight Fare Prediction using Machine Learning

A complete end-to-end Machine Learning project that predicts domestic flight ticket prices based on journey details, travel duration, number of stops, airline information, and route characteristics.

## 🚀 Live Demo

**Streamlit App:** https://flight-price-predictor-n7sm5hnqceuignbyeyjyny.streamlit.app/

---

## 📌 Project Overview

Flight ticket prices fluctuate based on multiple factors such as travel date, departure time, airline, duration, route, and number of stops. This project leverages Machine Learning techniques to predict flight fares accurately using historical flight data.

The project covers the complete ML lifecycle:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Building
* Ensemble Learning
* Model Evaluation
* Model Serialization
* Streamlit Deployment

---

## 🎯 Problem Statement

Predict the fare of a domestic flight based on:

* Journey Month
* Journey Day
* Weekday of Journey
* Departure Time
* Arrival Time
* Flight Duration
* Number of Stops
* Airline Information
* Source Airport
* Destination Airport

---

## 📊 Dataset

The dataset contains historical domestic flight information including:

| Feature         | Description                   |
| --------------- | ----------------------------- |
| Airline         | Airline operating the flight  |
| Source          | Departure city                |
| Destination     | Arrival city                  |
| Date of Journey | Flight travel date            |
| Departure Time  | Scheduled departure           |
| Arrival Time    | Scheduled arrival             |
| Duration        | Total travel duration         |
| Stops           | Number of layovers            |
| Price           | Flight fare (Target Variable) |

---

## 🔧 Feature Engineering

The following features were engineered from raw data:

### Date Features

* Journey Month
* Journey Day
* Journey Weekday

### Time Features

* Departure Hour
* Departure Minute
* Arrival Hour
* Arrival Minute

### Duration Features

* Duration Total Minutes

### Encoded Features

* Airline Encoding
* Source Encoding
* Destination Encoding

---

## 🤖 Machine Learning Models Used

The following regression models were evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Extra Trees Regressor
* Gradient Boosting Regressor

The best-performing model was selected based on evaluation metrics.

---

## 📈 Model Evaluation Metrics

Evaluation was performed using:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

### Performance Summary

| Metric   | Value          |
| -------- | -------------- |
| R² Score |   0.8615       |
| MAE      |   ₹1,118.2     |
| RMSE     |   ₹1,728.08    |

---

## 🖥️ Streamlit Application

The application allows users to:

* Enter flight details
* Select journey information
* Input travel duration and stops
* Generate fare predictions instantly

### Application Features

✅ Interactive User Interface

✅ Real-Time Predictions

✅ Feature Descriptions

✅ Input Validation

✅ Responsive Design

---

## 🏗️ Project Structure

```text
Flight-Fare-Predictor/
│
├── app.py
├── Data_Train.xlsx
├── Flight_Price_Prediction_Ensemble.ipynb
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
   ├── home_page.png
   └── prediction_page.png

```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/VINAY-160/Flight-Price-Predictor.git
```

Navigate to project folder:

```bash
cd Flight-Price-Predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit application:

```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Pickle

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📚 Key Learnings

* Data preprocessing and cleaning
* Feature engineering techniques
* Ensemble learning algorithms
* Model evaluation and comparison
* Model serialization using Pickle
* Building ML web applications with Streamlit
* End-to-end deployment workflow

---

## 🔮 Future Improvements

* Airline dropdown selection instead of encoded values
* Automated feature encoding
* Hyperparameter tuning dashboard
* Cloud deployment enhancements
* Route visualization
* Explainable AI (SHAP)

---

## 👨‍💻 Author

### Vinay Mishra

Integrated MCA Student
Data Science & Machine Learning Enthusiast

GitHub: https://github.com/VINAY-160

---

⭐ If you found this project useful, consider giving it a star.
