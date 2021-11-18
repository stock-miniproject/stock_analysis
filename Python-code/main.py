import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
from fbprophet import Prophet
from fbprophet.plot import plot_plotly


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction")

stocks = ("NKE", "GOOG", "MSFT", "GME", "SBUX", "TSLA", "RELI" , "DELL", "MCD", "AMZN", "PINS", "AAPL", "SPOT", "NFLX")
selected_stocks = st.selectbox("Select dataset from prediction",stocks)

n_years = st.slider("Years of predictioon:",1 ,5)
period = n_years * 365

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data..")
data = load_data(selected_stocks) 
data_load_state.text("Loading data...done!")

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Data'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Data'], y=data['Close'], name='stock_close'))
    fig.layput.update(title_text = "Time Series Data", xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)

#forecast

df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date":"ds","Close":"y"})


m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.write('Forecast data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)
