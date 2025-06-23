import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load predictions and evaluation metrics
with open("forecast_results.pkl", "rb") as f:
    data = pickle.load(f)
    multi_day_predictions = data["multi_day_predictions"]
    eval_results = data["eval_results"]

# Load actual vs predicted data if available
try:
    with open("actual_vs_predicted.pkl", "rb") as f:
        actual_pred_data = pickle.load(f)
except:
    actual_pred_data = None

# Streamlit page setup
st.set_page_config(page_title="LSTM Stock Forecast", layout="centered")
st.title("📈 AI-Powered Stock Forecast Dashboard")

with st.sidebar:
    st.header("🔍 Project Overview")
    st.markdown("""
    This dashboard showcases:
    - 📅 7-day LSTM forecasts for selected stocks
    - ✅ Evaluation metrics (RMSE, MAE)
    - 📊 Forecast trends
    - 📉 Actual vs predicted close comparisons
    
    Built using:
    - yfinance for data collection
    - Keras LSTM for modeling
    - Matplotlib + Streamlit for interactive UI
    """)

# 1. Forecast Table Viewer
st.header("📅 7-Day Forecasts")
for ticker, forecast in multi_day_predictions.items():
    with st.expander(f"{ticker} Forecast Table"):
        df_forecast = pd.DataFrame(forecast, columns=["Date", "Predicted Close"])
        df_forecast["Date"] = pd.to_datetime(df_forecast["Date"])
        df_forecast.set_index("Date", inplace=True)
        st.dataframe(df_forecast.style.format({"Predicted Close": "${:.2f}"}), height=200)

# 2. Model Accuracy Table
st.header("✅ Model Accuracy Summary")
st.dataframe(pd.DataFrame(eval_results).T.style.format("{:.2f}"), height=200)

# 3. Forecast Trend Viewer
st.header("📊 Forecast Trend Viewer")
selected_ticker = st.selectbox("Select a ticker to view forecast trend:", list(multi_day_predictions.keys()))
forecast = multi_day_predictions[selected_ticker]
df_plot = pd.DataFrame(forecast, columns=["Date", "Predicted Close"])
plt.figure(figsize=(7, 3.5))
plt.plot(df_plot["Date"], df_plot["Predicted Close"], marker='o', label="Forecast")
plt.xticks(rotation=45)
plt.title(f"{selected_ticker} – 7-Day Forecast")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# 4. Actual vs Predicted Viewer
st.header("📉 Actual vs Predicted Close Prices")
if actual_pred_data:
    ticker_choice = st.selectbox("Select ticker to compare:", list(actual_pred_data.keys()))
    data = actual_pred_data[ticker_choice]
    actual = data["actual"]
    predicted = data["predicted"]
    dates = pd.to_datetime(data["dates"])

    plt.figure(figsize=(7, 3.5))
    plt.plot(dates, actual, label="Actual", linewidth=2)
    plt.plot(dates, predicted, label="Predicted", linewidth=2, color='orange')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{ticker_choice} — Actual vs Predicted Close Prices")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)
else:
    st.warning("Actual vs predicted data not available. Upload actual_vs_predicted.pkl to enable this view.")
