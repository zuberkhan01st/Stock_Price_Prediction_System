# Crude Oil Stocks Price Prediction System

The **Stock Price Prediction System** is a Flask-based application that predicts **Brent Crude Oil Prices** using machine learning (Random Forest). The application also integrates **real-time data** from various sources like Yahoo Finance and Trading Economics to provide up-to-date insights for better decision-making.

---

## Features

### 1. **Brent Crude Oil Price Prediction**
- Predicts the price of Brent Crude Oil for the next day using a pre-trained **Random Forest** model.
- Input features include stock prices of major energy corporations, financial indices, and commodities such as silver and natural gas.
- Provides a highly accurate and scalable prediction based on historical data.

### 2. **Real-Time Data Integration**
- Fetches real-time data from multiple sources such as:
  - **Yahoo Finance**
  - **Economic Trading**
  - **Trading Economics**
- Includes data like stock prices, energy sector trends, and commodity prices to ensure accurate predictions.

### 3. **Today's Prediction**
- Displays the predicted price for Brent Crude Oil for the current day.
- Pulls data in real-time for accurate forecasting.

### 4. **Brent Crude Oil Market Data**
- Fetches today's Brent Crude Oil data, including:
  - **Open Price**
  - **Close Price**
  - **High and Low Prices**
  - **Trading Volume**

### 5. **API Endpoints**
The application exposes the following RESTful API endpoints:
---
*Processed Data*
![Data](./assets/Screenshot%202025-01-18%20221615.png)
---

*Predicted Crude Oil price*
![](./assets/Screenshot%202025-01-19%20102508.png)
---

*Raw data from Yahoo Finance*
![](./assets/Screenshot%202025-01-19%20110458.png)
---

*Crude Oil Related News Sentiment Analysis*
![](./assets/Screenshot%202025-01-21%20004020.png)
---
