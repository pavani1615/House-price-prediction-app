import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

# Load dataset
data = pd.read_csv("dataset/housing.csv")

# Features
X = data.drop("medianHouseValue", axis=1)
y = data["medianHouseValue"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBRegressor()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
score = r2_score(y_test, pred)
print("Model Accuracy:", score)

# Save model
joblib.dump(model, "model/house_model.pkl")