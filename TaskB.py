import numpy as n
import pandas as p
from matplotlib import pyplot as plt 
import datetime


df = p.read_csv('activity.csv')


interval = []
steps = []
for i in df['interval'].unique():
    interval.append(i)
    steps.append(df.loc[df['interval']==i, 'steps'].dropna().mean())


dfB = p.DataFrame({'interval':interval, 'steps':steps})
dfB.plot(x = 'interval', y = 'steps', kind = 'line')
plt.xticks(n.linspace(0,2355,15))
plt.title('avg no. of steps in 5min intervals')
plt.show()

print(f"interval with max no. of avg steps: {dfB.loc[dfB['steps']==dfB['steps'].max(), 'interval'].item()}")