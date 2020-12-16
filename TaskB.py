import numpy as n
import pandas as p
from matplotlib import pyplot as plt 
import datetime


a = p.read_csv('activity.csv')


interval = []
steps = []
for i in a['interval'].unique():
    interval.append(i)
    steps.append(a.loc[a['interval']==i, 'steps'].dropna().mean())


b = p.DataFrame({'interval':interval, 'steps':steps})
b.plot(x = 'interval', y = 'steps', kind = 'line')
plt.xticks(n.linspace(0,2355,15))
plt.title('avg no. of steps in 5min intervals')
plt.show()

print(f"interval with max no. of avg steps: {b.loc[b['steps']==b['steps'].max(), 'interval'].item()}")