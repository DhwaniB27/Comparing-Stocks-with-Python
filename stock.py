import yfinance as yf
import numpy as num
import pandas as pd
import statistics as st

def calculate(stocks, rfr=0.041) :
    rfr_monthly = pow((1+rfr),(1/12)) - 1
    for stock in stocks:
        df = yf.download(stock, period  = "5y",progress = False ,interval = "1mo" ,auto_adjust=False)
        result = {'return':[],'neg_return':[]}
        for i in range(1,len(df)):
            result['return'] += [(df["Adj Close"][stock].iloc[i] - df["Adj Close"][stock].iloc[i-1])/df["Adj Close"][stock].iloc[i-1]]
        result['mean'] = st.mean(result['return'])
        result['variance'] = st.variance(result['return'])
        result['stdev'] = st.stdev(result['return'])
        result['sharpe'] = (result['mean'] - rfr_monthly)/result['stdev']
        for i in result['return']:
            if i > 0 :
                result['neg_return'] += [0] 
            else:
                result['neg_return'] += [i]
        result['neg_stdev'] = st.stdev(result['neg_return'])
        result['sortino'] = (result['mean'] - rfr_monthly)/result['neg_stdev']
        print("The Sharpe Ratio for "+stock+" is ",result['sharpe'],"\nThe Sortino Ratio for "+stock+" is ",result['sortino'])

