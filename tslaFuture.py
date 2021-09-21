import pandas as pd 
from pandas.io.html import read_html   

url= 'https://en.wikipedia.org/wiki/History_of_Tesla,_Inc.#Timeline_of_production_and_sales'
classID = 'wikitable'
wiki = read_html(url, attrs={'class':classID})
wiki = wiki[0]
wiki = wiki['Totalsales[b]']

past_cars_sold = []
growth_rate = []
future_cars_sold = []

def past_growth():
    global past_cars_sold 
    global growth_rate
    global ave_growth_rate
    y = 33
    sales = 0
    for i in range(7):  #get cars sold from 2014-2020
        for x in range(4):
            sales = sales + int(wiki[y-x])
            f = y-x
        y = f - 1  
        past_cars_sold.append(sales)
        sales = 0 
    past_cars_sold.reverse() #cars sold from 2014-2020
    
    for i in range(len(past_cars_sold)-1):   
        y = ((past_cars_sold[i+1]-past_cars_sold[i])/past_cars_sold[i])
        growth_rate.append(round(y,2))
    ave_growth_rate = (sum(growth_rate)/len(growth_rate))+1    
    round(ave_growth_rate, 2)

def future_growth():
    past_growth()

    pe_ratio = 45 #Automobiles sectec avg pe ratio 58, tech sectec avg pe ratio 31
    avg_car_price = 36000
    operating_margin = .08 #snp500 avg 15%
    profit_margin = .70 #netincome/operatingincome APPL 86%, AMAZ 80%
    global ave_growth_rate
    global future_cars_sold
    global market_cap_cars
    global total_cars_sold

    future_cars = 0
    if ave_growth_rate > 1.50:
        ave_growth_rate = 1.30

    future_cars = ave_growth_rate*past_cars_sold[6]
    future_cars_sold.append(round(future_cars)) 
    for i in range(9):#cars sold form 2021-2030
        future_cars = (ave_growth_rate)*future_cars
        future_cars_sold.append(round(future_cars))    
    
    total_cars_sold = sum(future_cars_sold) #total cars sold from 2014-2030

    total_car_revune = future_cars_sold[9]*avg_car_price #car revune in 2030
    operating_income = total_car_revune * operating_margin #operating income 
    net_income = operating_income * profit_margin #net net income
    market_cap_cars = net_income * pe_ratio #market cap in 2030
    print('Market cap for the car side:',market_cap_cars)

#full self driving growth 
def fsd_growth():
 future_growth()

fsd_growth()

start = 2014
df = pd.DataFrame({'age':past_cars_sold+future_cars_sold,}, index = [start+i for i in range(17)])


