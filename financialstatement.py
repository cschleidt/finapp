import yfinance as yf  
  
# Define the ticker symbol for Apple Inc.  
ticker_symbol = "AAPL"  
  
# Create a ticker object for Apple Inc.  
ticker = yf.Ticker(ticker_symbol)  
  
# Get the financial data for the past 5 years  
financials_df = ticker.financials  
  
# Extract the required key figures for the past 5 fiscal years  
financial_data = financials_df[['Revenue', 'Net Income', 'Earnings Per Share', 'Total Assets', 'Total Liab']].head()  
  
# Convert the financial data to JSON format  
financial_data_json = financial_data.to_json()  
  
# Print the financial data in JSON format  
print(financial_data_json)  