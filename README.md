# 🏠 House Price Prediction Web App – README

## Project Overview

This project is a **House Price Prediction** application using **Python**, **Flask**, and **Linear Regression**.
It allows users to predict house prices based on features like area, bedrooms, bathrooms, main road, furnishing status, etc.

The app supports **two ways to give input**:

1. **Browser form** – Users select Yes/No options and enter numbers in the web page.
2. **API (Postman / JSON)** – Users can send a JSON request to get predicted prices programmatically.

---

## Features

* Linear Regression model trained on `Housing.csv`.
* Preprocessing includes:

  * Conversion of Yes/No columns to 1/0
  * One-hot encoding of `furnishingstatus`
* Predict house price for **new inputs**.
* Real-time predictions via:

  * Browser form
  * API endpoint (`/predict`)

---

## Installation

1. Make sure Python 3 is installed.
2. Install required packages:

```bash
pip install flask pandas scikit-learn
```

3. Place `Housing.csv` in the project folder.
4. Ensure project structure:

```
HousePriceProject/
│
├── app.py
├── Housing.csv
└── templates/
    └── index.html
```

---

## How to Run

1. Open terminal in project folder.
2. Run the Flask app:

```bash
python app.py
```

3. Flask will start at:

```
http://127.0.0.1:5000/
```

---

## Using Browser Form

1. Open browser: `http://127.0.0.1:5000/`
2. Fill in the form:

   * Numeric inputs: Area, Bedrooms, Bathrooms, Stories, Parking
   * Yes/No dropdowns: Main Road, Guest Room, Basement, Hot Water Heating, Air Conditioning, Preferred Area
   * Furnishing Status: Furnished / Semi-Furnished / Unfurnished
3. Click **Predict Price**
4. Predicted price will appear below the form.

---

## Using API (JSON)

* **Endpoint:** `POST http://127.0.0.1:5000/predict`
* **Content-Type:** `application/json`
* **Example JSON Request:**

```json
{
  "area": 3000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "yes",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 2,
  "prefarea": "yes",
  "furnishing": "unfurnished"
}
```

* **Example Response:**

```json
{
  "predicted_price": 5234567.89
}
```

---

## Notes

* The model is trained on **Housing.csv** and may need retraining for other datasets.
* The Yes/No fields are automatically converted to 1/0 before prediction.
* The application is suitable for demonstration, college projects, and small-scale house price prediction.

---
