# 📈 AI-Powered Stock Forecast Dashboard

A Streamlit dashboard that uses LSTM neural networks to forecast stock prices, compare actual vs predicted values, and visualize 7-day forward predictions with evaluation metrics.

https://ai-powered-stock-forecast-dashboard-fkhs8ewhwcdmyyqtpmywxr.streamlit.app/

---

## 🚀 Features
- ✅ 7-day forecasts using LSTM models
- 📉 Actual vs Predicted chart comparisons
- 📊 Interactive visualizations with Streamlit
- 🧠 Model accuracy metrics (RMSE, MAE)
- 📦 Pre-trained model data (`.pkl`) included

---

## 📁 Files
- `LSTM.ipynb` – Notebook to build and train LSTM models
- `lstm_dashboard.py` – Streamlit app to visualize results
- `forecast_results.pkl` – Contains forecasted values and metrics
- `actual_vs_predicted.pkl` – Stores historical actual vs predicted data
- `requirements.txt` – All dependencies to run the app

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run lstm_dashboard.py
