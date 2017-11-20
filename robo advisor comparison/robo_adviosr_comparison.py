import matplotlib.pyplot as plt
import numpy as np


## defines constant to change
Return = 0.07
years = 5
starting_tfsa = 5000
TFSA_cont = 5500
starting_rrsp = 10000
income = 75000
rrsp_cont = min(26000,income * 0.18)
starting_general = 5000
general_cont = 2000


##makes function to calaulate the year over year cost
def calculate(MER, AMF, balance, Trading_fee):
    new = balance*(1 + Return - MER) - AMF - Trading_fee
    tot_MER = (balance*(1 + Return) - new)/balance
    Tot_return = new/balance
    return new, tot_MER, Tot_return;

## aggregates for standard constant fee structue.  If they change Custom functions will be used
def aggregate(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    values[0] = calculate(MER, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            values[year] = calculate(MER, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
    return values



## RBC domionion secutires
def RBC_agg(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    TFSA = np.zeros ((years,3))
    TFSA[0] = starting_tfsa + TFSA_cont
    values[0] = calculate(MER, AMF + 0.01*TFSA[0,0], balance, trading_fee)
    for year in range(years):
        if year >0:
            TFSA[year] = calculate(MER, 0.01*TFSA[year-1,0], TFSA[year-1,0]+ TFSA_cont, trading_fee)
            values[year] = calculate(MER, AMF + 0.01*TFSA[year,0], values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
    return values







##wealth simple  assumes MER of 0.2%
def wealth_simple_agg(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance > 100000:
        values[0] = calculate(0.006, AMF, balance, trading_fee)
    else:
        values[0] = calculate(0.007, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont > 100000:
                values[year] = calculate(0.006, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            else:
                values[year] = calculate(0.007, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)               
    return values


## Nest wealth  webiste claims MER is 0.13%
def nest_wealth_agg(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance < 75000:
        values[0] = calculate(MER, 415, balance, trading_fee)
    elif balance < 150000 & balance:
        values[0] = calculate(MER, 655, balance, trading_fee)
    else:
        values[0] = calculate(MER, 1135, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 75000:
                values[year] = calculate(MER, 415, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 150000:
                values[year] = calculate(MER, 655, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)  
            else:
                values[year] = calculate(MER, 1135, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values

## says funds have an MER of 0.20% to 0.35%
def bmo_smartfolio_agg(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance < 100000:
        values[0] = calculate(0.009, AMF, balance, trading_fee)
    elif balance < 150000:
        values[0] = calculate(0.0084, AMF, balance, trading_fee)
    elif balance < 250000:
        values[0] = calculate(0.0077, AMF, balance, trading_fee)
    else:
        values[0] = calculate(0.00685, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 100000:
                values[year] = calculate(0.009, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 150000:
                values[year] = calculate(0.008, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)  
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 250000:
                values[year] = calculate(0.007, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
            else:
                values[year] = calculate(0.00685, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values



## wleathbar
def wealthbar(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if  balance < 150000:
        MER = (max(0,balance - 5000)*0.006)/balance
    elif balance < 500000:
        MER = (145000*0.006 + (balance-150000)*0.004)/balance
    else:
        MER = (145000*0.006 +350000*0.004 + (balance - 500000)*0.0035)/balance
    values[0] = calculate(MER, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
               if  balance < 150000:
                   MER = (max(0,balance - 5000)*0.006)/balance
               elif balance < 500000:
                   MER = (145000*0.006 + (balance-150000)*0.004)/balance
               else:
                   MER = (145000*0.006 +350000*0.004 + (balance - 500000)*0.0035)/balance 
        values[year] = calculate(0.0073, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values




## says MER range from 0.21 to 1.21%
def port_iq(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance < 100000:
        values[0] = calculate(0.009, AMF, balance, trading_fee)
    elif balance < 250000 & balance:
        values[0] = calculate(0.008, AMF, balance, trading_fee)
    elif balance < 500000 & balance:
        values[0] = calculate(0.007, AMF, balance, trading_fee)
    elif balance < 1000000 & balance:
        values[0] = calculate(0.006, AMF, balance, trading_fee)
    else:
        values[0] = calculate(0.0055, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 100000:
                values[year] = calculate(0.009, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 250000:
                values[year] = calculate(0.008, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)  
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 500000:
                values[year] = calculate(0.007, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 1000000:
                values[year] = calculate(0.006, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
            else:
                values[year] = calculate(0.0055, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values

## Modern advisor webiste sights that MER is 0.25% for underlying funds
def modern_ad(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance < 10000:
        values[0] = calculate(0.0025, AMF, balance, trading_fee)
    elif balance < 100000 & balance:
        values[0] = calculate(0.0075, AMF, balance, trading_fee)
    elif balance < 500000 & balance:
        values[0] = calculate(0.0065, AMF, balance, trading_fee)
    else:
        values[0] = calculate(0.006, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 10000:
                values[year] = calculate(0.0025, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 100000:
                values[year] = calculate(0.0075, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)  
            elif values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 500000:
                values[year] = calculate(0.0065, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
            else:
                values[year] = calculate(0.006, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values


## Just wealth MER's are assumed to be standard 0.25% listed on their website
def just_wealth(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    if balance < 500000:
        values[0] = calculate(0.0075, AMF, balance, trading_fee)
    else:
        values[0] = calculate(0.0065, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            if values[year-1,0] + TFSA_cont + rrsp_cont + general_cont < 500000:
                values[year] = calculate(0.0075, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
            else:
                values[year] = calculate(0.0065, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee) 
    return values


years = years + 1

## function calls
wealth_simple = wealth_simple_agg(0.006,0,starting_tfsa + starting_rrsp +starting_general, 0)
## takes my MER of 0.63% from my employer sunlife plan
sun_life = aggregate(0.0064,0,starting_tfsa + starting_rrsp +starting_general, 0)
## took a quated 2,25% from BMO's webiste
Mutual_fund = aggregate(0.0225,0,starting_tfsa + starting_rrsp +starting_general, 0)
##tangerine has 1.07% listed on their webiste.
tangerine = aggregate(0.0107,0,starting_tfsa + starting_rrsp +starting_general, 0)
DIY_ETF = aggregate(0.0016,0,starting_tfsa + starting_rrsp +starting_general, 60)
nestwealth = nest_wealth_agg(0.0013,0,starting_tfsa + starting_rrsp +starting_general, 300)
BMO_smartfolio = bmo_smartfolio_agg(0.009,0,starting_tfsa + starting_rrsp +starting_general,0)
Questrade_port_iq = port_iq(0.009,0,starting_tfsa + starting_rrsp +starting_general,0)
wealth_bar = wealthbar(0.009,0,starting_tfsa + starting_rrsp +starting_general,0)
modern_advisor = modern_ad(0.009,0,starting_tfsa + starting_rrsp +starting_general,0)
Just_wealth_port =just_wealth(0.009,0,starting_tfsa + starting_rrsp +starting_general,0)
## could not find invisors MER of underlying funds.  I will assume it's 0.18%
invisor = tangerine = aggregate(0.0068,0,starting_tfsa + starting_rrsp +starting_general, 0)
RBC_dom = RBC_agg(0.0018,125,starting_tfsa + starting_rrsp +starting_general, 300)


## makes list for the years list
year_list = []
for x in range(years):
    year_list.append(x)
    
    
# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)    
  
# You typically want your plot to be ~1.33x wider than tall. This plot is a rare    
# exception because of the number of lines being plotted on it.    
# Common sizes: (10, 7.5) and (12, 9)    
plt.figure(figsize=(12, 14))    
# Remove the plot frame lines. They are unnecessary chartjunk.    
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False) 


# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    

# Now that the plot is prepared, it's time to actually plot the data!    
# Note that I plotted the majors in order of the highest % in the final year.    
Adviosrs = ['Wealth Simple', 'Sun Life', 'Mutual funds', 'Tangerine', 'DIY ETFs',
            'Nest Wealth', 'BMO Smartfolio', 'Modern Advisor', 'Just Wealth', 
            'Invisor', 'RBC Domionion securities']

## set x to be 0 for value, 1 for MER and 3 for total return 
x=1
## total return
plt.plot(year_list, wealth_simple[:,x],lw=2.5, color=tableau20[0])
plt.plot(year_list, sun_life[:,x],lw=2.5, color=tableau20[1])
plt.plot(year_list, Mutual_fund[:,x],lw=2.5, color=tableau20[2])
plt.plot(year_list, tangerine[:,x],lw=2.5, color=tableau20[3])
plt.plot(year_list, nestwealth[:,x],lw=2.5, color=tableau20[4])
plt.plot(year_list, DIY_ETF[:,x],lw=2.5, color=tableau20[5])
plt.plot(year_list, BMO_smartfolio[:,x],lw=2.5, color=tableau20[6])
plt.plot(year_list, Questrade_port_iq[:,x],lw=2.5, color=tableau20[7])
plt.plot(year_list, wealth_bar[:,x],lw=2.5, color=tableau20[8])
plt.plot(year_list, modern_advisor[:,x],lw=2.5, color=tableau20[9])
plt.plot(year_list, Just_wealth_port[:,x],lw=2.5, color=tableau20[10])
plt.plot(year_list, invisor[:,x],lw=2.5, color=tableau20[11])
plt.plot(year_list, RBC_dom[:,x],lw=2.5, color=tableau20[12])




