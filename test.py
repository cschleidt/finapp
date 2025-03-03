import yfinance as yf
import json
 

stock = yf.Ticker("AAPL")
financials = stock.financials.T
balance_sheet = stock.balance_sheet.T
cashflow = stock.cashflow.T

key_metrics = {}

for year in financials.index[:5]:  # Last 5 years
    key_metrics[year.strftime('%Y')] = {
        'Revenue': financials.loc[year, 'Total Revenue'] if 'Total Revenue' in financials.columns else None,
        'Net Income': financials.loc[year, 'Net Income'] if 'Net Income' in financials.columns else None,
        'Total Assets': balance_sheet.loc[year, 'Total Assets'] if 'Total Assets' in balance_sheet.columns else None,
        'Operating Cash Flow': cashflow.loc[year, 'Total Cash From Operating Activities'] if 'Total Cash From Operating Activities' in cashflow.columns else None
    }

print(json.dumps(key_metrics, indent=4))