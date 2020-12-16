import numpy as n
import pandas as p
from matplotlib import pyplot as plt
import time

df = p.read_csv('activity.csv')


days = []
steps = []
for i in df['date'].unique():
    days.append(i)
    steps.append(df.loc[df['date']==i, 'steps'].dropna().sum())


dfA = p.DataFrame({'days':days, 'steps':steps})


ax = dfA.plot.bar(x='days', y='steps', width=0.5 , color='g')
plt.title('total no. of steps per day')
plt.xlabel('days')
plt.ylabel('steps')
plt.xticks(rotation = 45, size=7)
plt.show()


print("report: ")

print(f"mean: {dfA.mean().item()}")

print(f"median: {dfA.median().item()}")