import random
import plotly.express as px
count= []

dice_results=[]
for i in range (0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1+dice2)
    count.append(i)

fig = px.bar(x=dice_results,y=count)
fig.show()