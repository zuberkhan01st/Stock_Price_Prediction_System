import yfinance as yf
from datetime import datetime, timedelta

def get_oil_stock_price():
    """
    Fetch yesterday's stock price for Brent Crude oil (or an alternative).
    Returns the Open, Close, High, Low, and Volume data.
    """
    # Define alternative ticker symbols for Brent Crude Oil
    oil_symbols = ["BZ=F", "CL=F", "CO=F", "BRN=F"]
    
    oil_data = {
        "Date": "N/A",
        "Open": 0,
        "Close": 0,
        "High": 0,
        "Low": 0,
        "Volume": 0
    }
    
    for symbol in oil_symbols:
        try:
            # Fetch the data using yfinance for the past 2 days
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="5d")  # Fetch data for the past 2 days
            
            if not hist.empty:
                # Get the data for yesterday (the second-to-last entry)
                yesterday_data = hist.iloc[-2]
                oil_data = {
                    "Date": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),  # Date for yesterday
                    "Open": yesterday_data['Open'],
                    "Close": yesterday_data['Close'],
                    "High": yesterday_data['High'],
                    "Low": yesterday_data['Low'],
                    "Volume": yesterday_data['Volume']
                }
                break  # Exit loop if data is found

        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
    
    return oil_data


# Example usage
if __name__ == "__main__":
    oil_price_data = get_oil_stock_price()
    print("Yesterday's Brent Crude Oil Data:", oil_price_data)
