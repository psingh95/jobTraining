import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go

start = '2021-03-29'
end = '2021-09-11'

listofdf = []

tickers = ['CRM', 'NVDA']

for ticker in tickers:
    tickers_df = yf.download(ticker, start=start)
    tickers_df = tickers_df.rename({'Adj Close': ticker}, axis=1)
    listofdf.append(tickers_df[ticker])

stocks_data = pd.DataFrame(listofdf)
stocks_data = stocks_data.transpose()
listofdf.clear()

for ticker in tickers:
    listofdf.append(stocks_data[ticker]/stocks_data.iloc[0][ticker])
    
stocks_data = stocks_data.iloc[0:0]
stocks_data = pd.DataFrame(listofdf)
stocks_data = stocks_data.transpose()
stocks_data['Cum Return %'] = (((stocks_data[tickers[0]]+stocks_data[tickers[1]])/2) -1) *100


voo = yf.download('Voo',start,end)
voo['Cum Return'] = voo['Adj Close']/voo.iloc[0]['Adj Close']
voo['Cum Return %'] = (voo['Cum Return'] - 1) * 100

fig = go.Figure()
fig.add_trace(go.Scatter(x=voo.index, y=voo['Cum Return %'], name='Voo'))
fig.add_trace(go.Scatter(x=voo.index, y=stocks_data['Cum Return %'], name='Port'))
fig.update_layout(hovermode="x", template= "plotly_white")
fig.show()
