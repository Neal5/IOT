import pandas as pd
pd.DataFrame.read_sql()










# import yfinance as yf
# import pandas as pd

# # Load historical data in the past 10 years
# sp500 = yf.Ticker("^GSPC")
# end_date = pd.Timestamp.today()
# start_date = end_date - pd.Timedelta(days=10*365)
# sp500_history=sp500.history(start=start_date, end=end_date)

# # Remove unnecessary columns
# sp500_history = sp500_history.drop(columns=['Dividends', 'Stock Splits'])

# # Create a new column as Close 200 days moving average
# sp500_history['Close_200ma'] = sp500_history['Close'].rolling(200).mean()

# # Create a summary statistics table
# sp500_history_summary = sp500_history.describe()
# sp500_history_summary