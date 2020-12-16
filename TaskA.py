import numpy as n
import pandas as p
from matplotlib import pyplot as plt
import time

a = p.read_csv('activity.csv')

days = []
steps = []
for i in a['date'].unique():
    days.append(i)
    steps.append(a.loc[a['date']==i, 'steps'].dropna().sum())


b = p.DataFrame({'days':days, 'steps':steps})
ax = b.plot.bar(x='days', y='steps', width=0.5 , color='r')

plt.title('no. of steps/day')
plt.xlabel('days')
plt.ylabel('steps')
plt.xticks(rotation = 45, size=7)
plt.show()


print("report: ")
print(f"mean: {b.mean().item()}")
print(f"median: {b.median().item()}")