import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ===============================
# Load & Train Model
# ===============================
data = pd.read_csv("Housing.csv")

yes_no_cols = [
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning', 'prefarea'
]

for col in yes_no_cols:
    data[col] = data[col].map({'yes': 1, 'no': 0})

data = pd.get_dummies(data, columns=['furnishingstatus'], drop_first=True)

X = data.drop('price', axis=1)
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained")
print("R2 Score:", r2_score(y_test, model.predict(X_test)))

# ===============================
# Flask App
# ===============================
app = Flask(__name__)

# -------------------------------
# Browser Page
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------
# Browser Form Prediction
# -------------------------------
@app.route('/predict_form', methods=['POST'])
def predict_form():
    form = request.form

    # Convert yes/no to 1/0
    def yn(value):
        return 1 if value == 'yes' else 0

    furnishing = form['furnishing']

    new_house = pd.DataFrame([{
        'area': int(form['area']),
        'bedrooms': int(form['bedrooms']),
        'bathrooms': int(form['bathrooms']),
        'stories': int(form['stories']),
        'mainroad': yn(form['mainroad']),
        'guestroom': yn(form['guestroom']),
        'basement': yn(form['basement']),
        'hotwaterheating': yn(form['hotwaterheating']),
        'airconditioning': yn(form['airconditioning']),
        'parking': int(form['parking']),
        'prefarea': yn(form['prefarea']),
        'furnishingstatus_semi-furnished': 1 if furnishing == 'semi-furnished' else 0,
        'furnishingstatus_unfurnished': 1 if furnishing == 'unfurnished' else 0
    }])

    price = model.predict(new_house)[0]

    return render_template(
        'index.html',
        prediction=round(price, 2)
    )

# -------------------------------
# API Prediction (Postman)
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json

    new_house = pd.DataFrame([{
        'area': data['area'],
        'bedrooms': data['bedrooms'],
        'bathrooms': data['bathrooms'],
        'stories': data['stories'],
        'mainroad': data['mainroad'],
        'guestroom': data['guestroom'],
        'basement': data['basement'],
        'hotwaterheating': data['hotwaterheating'],
        'airconditioning': data['airconditioning'],
        'parking': data['parking'],
        'prefarea': data['prefarea'],
        'furnishingstatus_semi-furnished': data['semi_furnished'],
        'furnishingstatus_unfurnished': data['unfurnished']
    }])

    price = model.predict(new_house)[0]

    return jsonify({
        "predicted_price": round(float(price), 2)
    })

# ===============================
# Run App
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
