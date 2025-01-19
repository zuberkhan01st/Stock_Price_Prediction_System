import pickle
import pandas as pd
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from Services.get_real_time_data import get_todays_prediction, get_brent_crude_data as fetch_brent_crude_data
import yfinance as yf
import datetime

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return jsonify({'message':'Server is working'})

@app.route('/getprediction', methods=['GET'])
def prediction():
    try:
        # Load the saved model
        with open('C:/Users/ASUS Vivobook/Desktop/Mission_ACA/Stock_Price_Prediction_System/models/brent_crude_price_model.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)

        # Input data for prediction
        input_data = pd.DataFrame({
            'Date': ['20-12-2024'],  # Example Date
            'ExxonMobil Corporation_Close': [106.8700027],
            'Chevron Corporation_Close': [142.8500061],
            'ConocoPhillips_Close': [95.12000275],
            'Occidental Petroleum Corporation_Close': [47.13000107],
            'BP p.l.c._Close': [28.60000038],
            'Royal Dutch Shell_Close': [60.63999939],
            'United States Oil Fund_Close': [73.09999847],
            'Energy Select Sector SPDR Fund_Close': [83.43999481],
            'ProShares Ultra Bloomberg Crude Oil_Close': [25.98999977],
            'Natural Gas (Henry Hub)_Close': [3.747999907],
            'Brent Crude_Close': [72.94000244],
            'Silver_Close': [2628.699951],
            'Brent_Crude_Price': [29.65999985],
        })

        # Convert 'Date' to datetime and extract days since the start of dataset
        start_date = datetime(2020, 1, 1)  # Assuming the training data starts from 2020-01-01
        input_data['Date'] = pd.to_datetime(input_data['Date'])
        input_data['Date'] = (input_data['Date'] - start_date).dt.days  # Convert to number of days since start date

        # Make the prediction using the numerical data
        predicted_price = loaded_model.predict(input_data)

        # Return the prediction as a JSON response
        return jsonify({
            "Predicted Oil Price for the next day": f"{predicted_price[0]*(-1):.2f}"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/todays_prediction',methods=['GET'])
def todays_prediction():
    try:
        # Call the service to get today's prediction
        prediction_result = get_todays_prediction()

        # Return the prediction as a JSON response
        return jsonify(prediction_result)

    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)})

@app.route('/brute_crude_oil',methods=['GET'])
def get_brent_crude_data():
    """
    Fetch today's Brent Crude oil data: Open, Close, High, Low, and Volume.
    """
    
    data = fetch_brent_crude_data()  # Call the imported function
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
