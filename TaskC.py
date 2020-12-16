import pandas as p
import numpy as n
import datetime
from matplotlib import pyplot as plt
import statistics


a = p.read_csv('activity.csv')
print(p.isnull(a).sum())
b = a.fillna(0)
print(p.isnull(b).sum())

days = []
steps = []
for i in b['date'].unique():
    days.append(i)
    steps.append(b.loc[a['date']==i, 'steps'].sum())


plotx = p.DataFrame({'days':days, 'steps':steps})
ax = plotx.plot.bar(x='Days', y='Steps', width=0.5 , color='g')

plt.title('total no. of steps/day')
plt.xlabel('days')
plt.ylabel('steps')
plt.xticks(rotation = 45, size=7)
plt.show()

print("report:")
print(f"mean: {plotx.mean().item()}")
print(f"median: {plotx.median().item()}")