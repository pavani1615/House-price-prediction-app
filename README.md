# 🏠 House Price Prediction App

This is a **Machine Learning-based web application** built using **Streamlit** to estimate house prices based on location, size, demographics, and income.  

The app allows users to input house details and instantly get a predicted price in **USD** or **INR**.

---

## 🔗 Live Demo

Access the app here:  
[House Price Prediction App](https://house-price-prediction-app-nwshyhdbixnxjbvusk52sc.streamlit.app)

---

## 📂 Features

- **Country Selection:** India 🇮🇳 or USA 🇺🇸  
- **House Details Input via Dropdowns:**  
  - Longitude & Latitude (geographical location)  
  - Housing Median Age (years)  
  - Total Rooms, Total Bedrooms  
  - Population, Households  
  - Median Income (income of residents, in 10k USD)  
  - Ocean Proximity (distance from sea)  
- **Predict House Price:** Automatically converts to INR if India is selected  
- **Professional and clean UI using Streamlit**

---

## 📁 Dataset

- **File:** `dataset/housing.csv`  
- **Description of columns:**
  - `longitude` → Location east/west  
  - `latitude` → Location north/south  
  - `housingMedianAge` → Median age of houses in the area  
  - `totalRooms` → Total rooms in the houses  
  - `totalBedrooms` → Total bedrooms in the houses  
  - `population` → Number of people living in the area  
  - `households` → Number of households in the area  
  - `medianIncome` → Income of residents (in 10k USD)  
  - `medianHouseValue` → Target variable: House price in USD  
  - `oceanProximity` → Distance from ocean  

> The dataset is used to train the **Linear Regression model** saved in `model/house_model.pkl`.

---

## 🛠 Technology Stack

- **Frontend & Deployment:** Streamlit  
- **Machine Learning:** Scikit-Learn (Linear Regression)  
- **Data Handling:** Pandas, NumPy  
- **Model Serialization:** Joblib  
- **Python Version:** 3.14  

---

## ⚙️ Installation & Running the App (Local Setup)

1. Clone the repository:

```bash
git clone https://github.com/pavani1615/House-price-prediction-app.git
cd House-price-prediction-app
