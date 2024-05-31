import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

# Custom CSS for the entire webpage
custom_css = """
    <style>
        body {
            background-color: #222;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: white;
        }
    </style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Function to load stock data
def load_data(symbol, start, end):
    data = yf.download(symbol, start, end)
    return data

# Function to plot moving averages
def plot_moving_averages(data, ma1, ma2):
    ma_1_days = data.Close.rolling(ma1).mean()
    ma_2_days = data.Close.rolling(ma2).mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('black')  # Set background color to black
    ax.plot(data.Close, label='Close Price', color='green')
    ax.plot(ma_1_days, label=f'MA{ma1}', color='red')
    ax.plot(ma_2_days, label=f'MA{ma2}', color='blue')
    ax.set_xlabel('Date', color='white')
    ax.set_ylabel('Price', color='white')
    ax.set_title('Price vs Moving Averages', color='white')
    ax.legend()
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    st.pyplot(fig)

# Sidebar
st.sidebar.title('Stock Market Predictor')
stock = st.sidebar.text_input('Enter Stock Symbol', 'GOOG')
start = st.sidebar.date_input('Start Date', pd.to_datetime('2012-01-01'))
end = st.sidebar.date_input('End Date', pd.to_datetime('2022-12-31'))

# Main content
st.title('Stock Market Predictor')

data = load_data(stock, start, end)

st.subheader('Stock Data')
st.write(data)

st.subheader('Price vs Moving Averages')
ma1 = st.slider('Select MA1:', min_value=5, max_value=100, value=50, step=5)
ma2 = st.slider('Select MA2:', min_value=10, max_value=200, value=100, step=10)

plot_moving_averages(data, ma1, ma2)