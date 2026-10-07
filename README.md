# Comparing Stocks with Python

To compare stocks using Sharpe and Sortino Ratios in Python

## Description

Stocks can be compared in many different ways, 2 of these are the Sharpe ratio and the Sortino Ratio. Here we are calculating the Sharpe and Sortino ratios for stocks on the basis of the adjusted closing values of the past 5 years.

### Sharpe Ratio
This ratio is used to compare the returns of a stock with its risk. We do so by setting a benchmark, finding the difference between the returns and the benchmark and devide by the standard deviation of the return, which is a measure of the volatility. It is measured as follows:

$$
\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
$$

where:

- $R_p$ = return of portfolio
- $R_f$ = risk-free rate
- $\sigma_p$ = standard deviation of the portfolio's excess return

### Sortino Ratio
The formula for the Sharpe ratio's standard deviation assumes that price changes in both directions carry the same level of risk. For most investors and analysts, the risk of an unusually low return contrasts sharply with the chance of an unusually high return. A modified version of the Sharpe, known as the Sortino ratio, disregards above-average gains to concentrate only on downside volatility as a more accurate representation of the risk associated with a stock. The standard deviation found in the denominator of a Sortino ratio assesses the variability of negative returns or those under a specified benchmark in relation to the average of these returns. It is measured as follows:

$$
\text{Sortino Ratio} = \frac{R_p - R_f}{\sigma_d}
$$

where:

- $R_p$ = return of portfolio
- $R_f$ = risk-free rate
- $\sigma_d$ = standard deviation of the downside

### Interpretation

Sharpe ratios above one are generally considered “good,” offering excess returns relative to volatility. However, investors often compare the Sharpe ratio of a portfolio or fund with that of its peers or market sector. So a portfolio with a Sharpe ratio of one might be found lacking if most rivals have ratios above 1.2.
A higher Sortino ratio result is better, just like the Sharpe ratio. When looking at two similar investments, a rational investor would prefer the one with the higher Sortino ratio because it means that the investment is earning more return per unit of the bad risk that it takes on.
Sharpe measures return compared with overall risk, while Sortino measures return compared with downside risk only. Since Sortino ignores positive fluctuations, it is usually higher than Sharpe.

## How to Use

* install all libraries listed in requirements.txt
* you may call on the function by the name of calculate with list of stock tickers(you may put in 1 or more) as parameter, you may also put in a second parameter, the risk free rate per annum. If risk free rate is not mentioned, it is assumed to be 4.1% pa in line with the US treasury bonds at the time of  writing this code.
```
calculate(["ticker for stock 1","ticker for stock 2"], risk_free_rate_pa)
```
## Example
On calling 
```
calculate(["AAPL","MSFT"])
```
I recive the following output
```
The Sharpe Ratio for AAPL is  0.16158848669013973 
The Sortino Ratio for AAPL is  0.343539942854589
The Sharpe Ratio for MSFT is  0.10637228358980028 
The Sortino Ratio for MSFT is  0.21736478021472228
```
This shows the Sharpe and Sortino ratios for both Apple and Microsoft. we see that Microsoft has a lower Sharpe and Sortino ratio than Apple. This suggests that Apple generated better returns relative to the amount of risk taken during this period



