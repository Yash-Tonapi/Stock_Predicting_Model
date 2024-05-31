# Stock Market Predictor using LSTM

This repository contains code for a stock market predictor utilizing Long Short-Term Memory (LSTM) neural networks. The predictor utilizes historical stock data to forecast future prices. Below are the components of this repository:

## Files Included:
1. Jupyter Notebook - Stock_Predictor_LSTM.ipynb: This notebook contains the code to train the LSTM model using historical stock data. It includes data preprocessing, model training, and evaluation. The trained model is saved for future use.

2. app.py: This Python script creates a Streamlit web application for the stock market predictor. It allows users to input a stock symbol and date range, visualize stock data, and adjust moving average parameters for analysis.

3. requirements.txt: This file lists all Python dependencies required to run the code.

README.md: This Markdown file provides instructions on how to use the repository, including installation steps and usage guidelines.


## Usage Instruction
To use the stock market predictor:

1. Clone this repository to your local machine.
```bash
git clone https://github.com/Tejaspatil06/Stock_Predicting_Model_Using_LSTM.git
```
2. Install the required Python dependencies.
```bash
pip install -r requirements.txt
```
3. Run the Streamlit web application.
```bash
streamlit run app.py
```
4.Enter a stock symbol and date range in the sidebar to visualize stock data and adjust moving average parameters for analysis.

## Additional Information:

1. Data Source: The stock data is obtained using the Yahoo Finance API (yfinance).
2. Model: The predictor employs a stacked LSTM architecture for time-series forecasting.
3. Visualization: Matplotlib is used for data visualization within the Streamlit application.
4. Customization: Feel free to customize the code according to your requirements or extend the functionality as needed.

## Acknowledgments:

1. Streamlit for creating an intuitive web application framework.
2. Matplotlib for data visualization capabilities.
3. yfinance for providing access to Yahoo Finance data.
4. Keras for building and training the LSTM model.
