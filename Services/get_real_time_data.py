import pickle
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

# Define stock symbols corresponding to the columns in your dataset
symbols = [
    ("ExxonMobil Corporation", "XOM"),
    ("Chevron Corporation", "CVX"),
    ("ConocoPhillips", "COP"),
    ("Occidental Petroleum Corporation", "OXY"),
    ("BP p.l.c.", "BP"),
    ("Royal Dutch Shell", "SHEL"),
    ("United States Oil Fund", "USO"),
    ("Energy Select Sector SPDR Fund", "XLE"),
    ("ProShares Ultra Bloomberg Crude Oil", "UCO"),
    ("Natural Gas (Henry Hub)", "NG=F"),
    ("Brent Crude", "BZ=F"),
    ("Gold", "GC=F"),
    ("Silver", "SI=F")
]

MODEL_PATH = 'C:/Users/ASUS Vivobook/Desktop/Mission_ACA/Stock_Price_Prediction_System/models/brent_crude_price_model.pkl'

def fetch_todays_data():
    """
    Fetch today's stock data for required symbols using yfinance.
    """
    today_data = {}
    for name, symbol in symbols:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")  # Fetch today's data

        # Ensure data is available; if not, use 0 as fallback
        today_data[f"{name}_Close"] = hist['Close'].iloc[-1] if not hist.empty else 0

    # Add today's date
    today_data['Date'] = datetime.now().strftime('%Y-%m-%d')

    return today_data


def prepare_input_data(today_data):
    """
    Prepare the input data for the prediction model.
    """
    # Convert data to DataFrame
    input_data = pd.DataFrame([today_data])

    # Define the exact required columns as per the model's training features
    required_columns = [
        "Date", "ExxonMobil Corporation_Close", "Chevron Corporation_Close", "ConocoPhillips_Close",
        "Occidental Petroleum Corporation_Close", "BP p.l.c._Close", "Royal Dutch Shell_Close",
        "United States Oil Fund_Close", "Energy Select Sector SPDR Fund_Close",
        "ProShares Ultra Bloomberg Crude Oil_Close", "Natural Gas (Henry Hub)_Close", "Brent Crude_Close",
        "Gold_Close", "Silver_Close"
    ]

    # Ensure all required columns are in the input data
    for column in required_columns:
        if column not in input_data:
            input_data[column] = 0  # Add missing columns with default value

    # Convert 'Date' to days since the start of the dataset
    start_date = datetime(2020, 1, 1)  # Assuming training data starts from 2020-01-01
    input_data['Date'] = pd.to_datetime(input_data['Date'])
    input_data['Date'] = (input_data['Date'] - start_date).dt.days

    return input_data[required_columns]  # Ensure columns are in the correct order


def make_prediction(input_data):
    """
    Make a prediction using the pre-trained model.
    """
    with open(MODEL_PATH, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # Use the model to predict Brent Crude Tomorrow Price
    predicted_price = loaded_model.predict(input_data)
    return predicted_price[0]


def get_todays_prediction():
    """
    Fetch today's data, prepare input, and predict Brent Crude Tomorrow Price.
    """
    today_data = fetch_todays_data()  # Fetch data for today
    input_data = prepare_input_data(today_data)  # Prepare the input
    predicted_price = make_prediction(input_data)  # Get the prediction

    # Return the prediction and today's data
    return {
        "Predicted Brent Crude Tomorrow Price": f"{predicted_price:.2f}",
        "Todays Data": today_data
    }


def get_brent_crude_data():
    """
    Fetch today's Brent Crude oil data: Open, Close, High, Low, and Volume.
    """
    brent_crude_symbol = "BZ=F"
    ticker = yf.Ticker(brent_crude_symbol)
    
    # Check if today is a weekend (Saturday or Sunday)
    today = datetime.now()
    if today.weekday() >= 5:  # Saturday (5) or Sunday (6)
        # Get data for the previous Friday
        last_trading_day = today - timedelta(days=today.weekday() - 4)  # Move back to Friday
    else:
        # Today is a weekday, so use the current date
        last_trading_day = today
    
    # Fetch data for the last available 5 days
    hist = ticker.history(start=(last_trading_day - timedelta(days=5)).strftime('%Y-%m-%d'), end=last_trading_day.strftime('%Y-%m-%d'))  # Fetch the past 5 days of data

    # Ensure data is available, otherwise use 0 as fallback
    if not hist.empty:
        brent_crude_data = {
            "Date": datetime.now().strftime('%Y-%m-%d'),
            "Open": hist['Open'].iloc[-1].item(),  # Convert to standard int/float
            "Close": hist['Close'].iloc[-1].item(),  # Convert to standard int/float
            "High": hist['High'].iloc[-1].item(),  # Convert to standard int/float
            "Low": hist['Low'].iloc[-1].item(),  # Convert to standard int/float
            "Volume": hist['Volume'].iloc[-1].item()  # Convert to standard int/float
        }
    else:
        brent_crude_data = {
            "Date": "N/A",
            "Open": 0,
            "Close": 0,
            "High": 0,
            "Low": 0,
            "Volume": 0
        }

    return brent_crude_data

# Example usage
if __name__ == "__main__":
    prediction = get_todays_prediction()
    print("Today's Prediction:", prediction["Predicted Brent Crude Tomorrow Price"])
    print("Today's Data:", prediction["Todays Data"])
