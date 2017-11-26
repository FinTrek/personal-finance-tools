# Robo Advisor Comparison tool

Note this was a fun side project and not meant to reflect professional financial advice.

I Made a tool that compares the cost of the common Robo advisors in Canada.  The tools only compares costs for investors looking to find the cheapest robo advisors.  Note that I have included a RBC Dominion Securities and DIY ETF portfolio's.  These aren't perfectly comparisons since they offer different services (more or less planning).  When using this tool please think holistically about the advice/expertise you need and what you're willing to pay for that.

## How to Use
In the top of the script in the Jupyter notebook or the Python script input the account details you have. For starters I have details to be chosen somewhat arbitrarily to start with.

```python
## defines constant to change
##you can customize these to your own portfolio
Return = 0.06
years = 5
starting_tfsa = 5000
TFSA_cont = 5500
starting_rrsp = 50000
income = 75000
rrsp_cont = min(26000,income * 0.18)
starting_general = 1000
general_cont = 2000
```

Now simply run through the script you will generate a few things that will aid you in making a decision. The first is a summary of the your portfolio values over the time period specified.  The second is how the total effective MER changes over that period.  If you would like a simple list of the values you can find that at the end of the programs output as well.


<p align="center">
  <img src=images/Total%20Value%20Difference.png alt="overview" style="width: 600px;" style="height: 200px;"/>
</p>

<p align="center">
  <img src=images/MER%20fee%20distribution.png alt="overview" style="width: 600px;" style="height: 200px;"/>
</p>


Lastly, feel free to add TD-Esereis, RBC Dominion Securities Sunlife, Tangerine, Mutual Funds, and DIY yourself investing in ETFs into this file.  It will give you a sense of what other none Robo Advisors are charging.

Please feel free to open any issues or ask any questions.

Cheers,

Winston
