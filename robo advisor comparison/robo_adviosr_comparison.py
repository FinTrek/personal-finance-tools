import matplotlib.pyplot as plt
import numpy as np


## defines constant to change
Return = 0.07
years = 25
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

def aggregate(MER, AMF, balance, trading_fee):
    values = np.zeros( (years,3) )
    values[0] = calculate(MER, AMF, balance, trading_fee)
    for year in range(years):
        if year >0:
            values[year] = calculate(MER, AMF, values[year-1,0] + TFSA_cont + rrsp_cont + general_cont, trading_fee)
    return values


## wealth simple
wealth_simple = aggregate(0.006,0,starting_tfsa + starting_rrsp +starting_general, 0)
sun_life = aggregate(0.0064,0,starting_tfsa + starting_rrsp +starting_general, 0)
Mutual_fund = aggregate(0.0235,0,starting_tfsa + starting_rrsp +starting_general, 0)
tangerine = aggregate(0.0107,0,starting_tfsa + starting_rrsp +starting_general, 0)

        


## makes list for the years list
year_list = []
for x in range(years):
    year_list.append(x)

## total return
plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.plot(year_list, wealth_simple[:,0])
plt.plot(year_list, sun_life[:,0])
plt.plot(year_list, Mutual_fund[:,0])
plt.plot(year_list, tangerine[:,0])


##Total MER
plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.plot(year_list, wealth_simple[:,1])
plt.plot(year_list, sun_life[:,1])
plt.plot(year_list, Mutual_fund[:,1])
plt.plot(year_list, tangerine[:,1])

##Total return
plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.plot(year_list, wealth_simple[:,2])
plt.plot(year_list, sun_life[:,2])
plt.plot(year_list, Mutual_fund[:,2])
plt.plot(year_list, tangerine[:,2])

