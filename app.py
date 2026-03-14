import streamlit as st
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load trained model
model = joblib.load("model/house_model.pkl")

# Page setup
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction App")
st.markdown(
    "Estimate house prices based on area, size, and demographics. "
    "Select values below and click **Predict Price**."
)

st.divider()

# Country selection
country = st.selectbox("Select Country", ["India 🇮🇳", "USA 🇺🇸"])

st.subheader("🏡 House Details")

# Columns for layout
col1, col2 = st.columns(2)

with col1:
    longitude_options = [round(x, 2) for x in np.linspace(-125, -65, 61)]
    longitude = st.selectbox("Longitude (East-West position)", longitude_options)

    latitude_options = [round(x, 2) for x in np.linspace(25, 50, 51)]
    latitude = st.selectbox("Latitude (North-South position)", latitude_options)

    age_options = list(range(1, 53))
    age = st.selectbox("Housing Median Age (Median age of houses in the area)", age_options)

    # Country-aware income label
    if country == "India 🇮🇳":
        income_label = "Median Income (Income of residents, in ₹ Lakh)"
        income_options = [i*1 for i in range(1, 201)]  # 1 Lakh to 200 Lakh
    else:
        income_label = "Median Income (Income of residents, in 10k USD)"
        income_options = [round(x * 0.5, 2) for x in range(1, 41)]  # 0.5 to 20 10k USD

    income = st.selectbox(income_label, income_options)

with col2:
    rooms_options = list(range(2, 101))
    rooms = st.selectbox("Total Rooms (Number of rooms in the house)", rooms_options)

    bedrooms_options = list(range(1, 51))
    bedrooms = st.selectbox("Total Bedrooms (Number of bedrooms in the house)", bedrooms_options)

    population_options = list(range(1, 2001, 10))
    population = st.selectbox("Population (Number of people living in the area)", population_options)

    households_options = list(range(1, 1001, 5))
    households = st.selectbox("Households (Number of separate households)", households_options)

# Ocean Proximity
ocean_proximity = st.selectbox(
    "Ocean Proximity (Distance from the sea)",
    ["<1H OCEAN", "INLAND", "NEAR BAY", "NEAR OCEAN", "ISLAND"]
)

st.divider()

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[longitude, latitude, age, rooms,
                            bedrooms, population, households, income]])

    # Make prediction
    price_usd = model.predict(input_data)[0]
    usd_to_inr = 83
    price_inr = price_usd * usd_to_inr

    # Reasonableness check (example dataset bounds)
    min_price = 50000   # replace with your dataset min
    max_price = 1000000 # replace with your dataset max

    st.subheader("💰 Predicted House Price")
    if country == "India 🇮🇳":
        st.success(f"Estimated Price: ₹{price_inr:,.0f}")
    else:
        st.success(f"Estimated Price: ${price_usd:,.2f}")

    if price_usd < min_price or price_usd > max_price:
        st.warning("⚠️ Predicted price seems unusual. Please check your input values.")

    # Optional: Evaluation metrics (Step 2)
    st.subheader("📊 Model Evaluation Metrics (Optional)")
    st.info("You can enter actual prices for test data to calculate metrics.")

    # User inputs for actual prices for evaluation
    y_true_str = st.text_area(
        "Enter actual prices (comma-separated, same order as predicted data)", 
        value="300000, 450000, 500000"
    )
    y_pred_str = st.text_area(
        "Enter predicted prices (comma-separated, same order as actual prices)", 
        value="310000, 460000, 480000"
    )

    if st.button("Calculate Evaluation Metrics"):
        try:
            y_true = np.array([float(x.strip()) for x in y_true_str.split(",")])
            y_pred = np.array([float(x.strip()) for x in y_pred_str.split(",")])

            mae = mean_absolute_error(y_true, y_pred)
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))
            r2 = r2_score(y_true, y_pred)

            st.success(f"MAE: {mae:,.2f}")
            st.success(f"RMSE: {rmse:,.2f}")
            st.success(f"R² Score: {r2:.2f}")
        except Exception as e:
            st.error(f"Error: {e}. Please check your input format.")