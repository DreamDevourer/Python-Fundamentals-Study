import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # Nick Stock Tracker
    Here is all targets for the next 6 months.
    """
)

# Documentation from https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticker symbol, get data from it and history.
# How this will show up:
# Open -> High -> Low -> Close -> Volume -> Dividends -> Stock -> Splits
# streamlit run stock_data_driven_web_app.py

"""
## HubSpot Global

### Market Open/Close
"""
stockCode = 'HUBS'
stockData = yf.Ticker(stockCode)
stockHistory = stockData.history(
    period='1d', start='2019-01-01', end='2021-09-01')

st.line_chart(stockHistory.Close)
"""
### Market Volume
"""
st.line_chart(stockHistory.Volume)


"""
## Qualcomm Inc. Global

### Market Open/Close
"""
stockCode = 'QCOM'
stockData = yf.Ticker(stockCode)
stockHistory = stockData.history(
    period='1d', start='2018-01-01', end='2021-09-01')

st.line_chart(stockHistory.Close)
"""
### Market Volume
"""
st.line_chart(stockHistory.Volume)


"""
## Electronic Arts Inc. Global

### Market Open/Close
"""
stockCode = 'EA'
stockData = yf.Ticker(stockCode)
stockHistory = stockData.history(
    period='1d', start='2000-01-01', end='2021-09-01')

st.line_chart(stockHistory.Close)
"""
### Market Volume
"""
st.line_chart(stockHistory.Volume)
