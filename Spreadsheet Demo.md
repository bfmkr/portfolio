---
layout: default
title: Spreadsheet Demo
---

# Spreadsheet Demo 

&nbsp;

In this demo I investigate the monthly prices of the fictional stock ABC over a 3 year period, calculate simple risk and reward metrics, compare the distribution to a theoretical Gaussian model, and compare the performance to the US market index as a benchmark over the same period.
The full details are available to view and download [here](https://docs.google.com/spreadsheets/d/1siknL7tF3BhBewxQRVH1tyg2vGfkvemDQxeHJDNO5k0/edit?usp=sharing).

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSGCOtI0NUWpgbHzTx1VXQdDCAQaImQRU9JR9SoJnaRovRmytICbSMLqSJkPJd2IzivHEML0-tHsq27/pubhtml?gid=558173804&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="640"></iframe>
<figcaption style="text-align: center; font-style: italic;">
    Fig. 1 Financial Analytics for the fictional stock ABC. 
    For a best viewing experience, open the full workbook <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSGCOtI0NUWpgbHzTx1VXQdDCAQaImQRU9JR9SoJnaRovRmytICbSMLqSJkPJd2IzivHEML0-tHsq27/pubhtml" title="Financial analytics spreadsheet demo"> here</a> in a new tab.
</figcaption>


## Breakdown of results

### Monthly stock analysis

The simplest thing we can do with the raw data is probably a line chart of the monthly stock prices, *Fig 2*. 
There is an upward trend from the lowest price, $43.63, recorded on 2015-08-31, to the high price, $59.89, recorded on 2016-09-31.

<div style="text-align: center;">
<iframe width="506" height="313" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSGCOtI0NUWpgbHzTx1VXQdDCAQaImQRU9JR9SoJnaRovRmytICbSMLqSJkPJd2IzivHEML0-tHsq27/pubchart?oid=1909742734&amp;format=interactive"></iframe>
</div>
<figcaption style="text-align:center; font-style: italic;">
    Fig. 2 Line chart of historical prices for the stock ABC
</figcaption>

*Fig. 3* displays a bar chart of the % monthly returns grouped by month. 
Plotting this gives us a quick way to see if there is any particular time of year that the stock does particularly well (or poorly).
To generate this plot the **% monthly returns** were computed in a standard way (described later), and the built-in function `COUNTIFS()` and `MONTH()` were used to find the total positive and negative returns from the 3 years of data.

<div style="text-align: center;">
<iframe width="506" height="313" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSGCOtI0NUWpgbHzTx1VXQdDCAQaImQRU9JR9SoJnaRovRmytICbSMLqSJkPJd2IzivHEML0-tHsq27/pubchart?oid=499677409&amp;format=interactive"></iframe>
</div>
<figcaption style="text-align:center; font-style: italic;">
    Fig. 2 November stands out as a good time of year
</figcaption>


### Reward metrics

As alluded to above, the **percentage return** gives an idea of the amount of money you make, or would potentially make, on an investment over a period of time.
We can keep track of the investment by computing the **series of historical returns** \\( \\{ R_{1}, R_{2}, R_{3}, \dots, R_{N} \\}\\) on a monthly basis, and this represents the potential amount of money made from month to month.

In plain English,

\begin{equation}
\text{ % monthly return } = \frac{\text{final value } + \text{cash flows } - \text{initial value}}{\text{initial value}} \times 100.
\end{equation}


The minimum potential return is -100% of the initial investment while the maximum is unbounded.
These values also take into account any cash-flow received while holding the investment, i.e. dividends. 

Given the series of historical returns, and the capital invested \\( C \\), the **return on the investment** after \\( T\\) months is  \\( C(1+R_{1})(1+R_{2})\dots(1+R_{T}) \\). 
Here \\( R_{1} \\) represents the first % monthly return from when the capital is initially invested.
In plain English, this is the compounding effect of 

\\[
 \text{wealth} = \text{wealth of previous month} \times (1 + \text{ % monthly return} ) 
\\]

The **effective rate of return** \\( R_{E}\\) is a useful metric for evaluating the overall return on an investment. 
Mathematically it is the rate of the return such for the capital invested \\( C \\), the final cumulative wealth can be calculated by \\( C(1+ R_{E})^{T}\\) after \\(T\\) months. 
The cumulative wealth for the stock ABC given an initial \\(C = \$ 100.00 \\) is plotted in *Fig. 3* alongside an equivalent investment for the US market index, i.e. the comparable result by investing in the average performance of major companies traded in the US stock market. 

<div style="text-align: center;">
<iframe width="506" height="313" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSGCOtI0NUWpgbHzTx1VXQdDCAQaImQRU9JR9SoJnaRovRmytICbSMLqSJkPJd2IzivHEML0-tHsq27/pubchart?oid=1610569546&amp;format=interactive"></iframe>
</div>
<figcaption style="text-align: center; font-style: italic;">
     Fig. 3 The benchmark outperformed the stock until Q1 of 2016. 
     After that, ABC went above the average performance of the stock market as a whole.
</figcaption>

Finally the **average rate of return** is simply the arithmetic mean of the series of historical returns, computed in the spreadsheet using `AVERAGE()`.
It therefore considers all returns to be independent, and, loosely speaking, can be used to infer the expected reward for future performance.

|

### Comparison to the theoretical Gaussian model


## Details of calculations

### Monthly returns

The series of % monthly returns were calculated in the standard way. In plain English,

\begin{equation}
\text{ % monthly return } = \frac{\text{final value } + \text{cash flows } - \text{initial value}}{\text{initial value}} \times 100.
\end{equation}

In contrast, for calculating the % monthly returns for the US market index for benchmarking purposes, no dividends contribute to the dollar return in the numerator, so \\( \text{ cash flows } = 0 \\) in that case.

### Reward Metrics

To calculate  the effective rate of return \\(R_{E}\\), we can invert the defining equation 

\\[
C(1+R_{1})(1+R_{2})\dots(1+R_{T}) = C(1+ R_{E})^{T},
\\]

to find

\\[ 
 R_{E} = -1 + [(1+R_{1})(1+R_{2})\dots(1+R_{T})]^{1/T}
\\]

which is simply \\(-1\\) plus the geometric mean of \\(1+ \text{monthly return} \\). 
This is compactly calculated in the spreadsheet with `=ARRAYFORMULA(GEOMEAN(1+ cell_range)-1)` where `cell_range` contains the series of monthly returns.


### Risk metrics

The **volatility** for stock ABC was computed as a sample standard deviation \\( \sigma \\) of the series of \\( N \\) historical returns \\( R_{i} \\)

\\[
\sigma = \sqrt{\frac{\sum_{i=1}^{N} (R_{i}-\mu)^{2}}{N-1}}
\\]

in which \\( \mu = \sum_{i=1}^{N} R_{i} / N \\) is the average return.
This was executed in the spreadsheet with the inbuilt function `STDEV()`.



<script>
MathJax = {
  svg: {
    fontCache: 'global'
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>

