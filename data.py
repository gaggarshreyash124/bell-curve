import random 
import csv
import plotly.express as px
import plotly.figure_factory as pff


diceresult = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)

fig = px.bar(x=diceresult,y=count)
fig = pff.create_distplot([diceresult],["result"],show_hist = False)

fig.show()