# this is used in when we have atleast 2 columns of data
# this s used when we have atleast one numeric column and one categorical column
# but we also can use in numeric and numeric column
# we mostly used in time series data

# price of iphone

from operator import index
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data=pd.read_csv('sharma-kohli.csv')
# price = [100, 200, 300, 400, 80, 190, 330]
# year=[2015, 2016, 2017, 2018, 2019, 2020, 2021]

# plt.plot(year,price)
# plt.show()

data=pd.read_csv('sharma-kohli.csv')
# print(data.sample())
# print(data.info())

# print(data)
# plt.plot(data[index],data['V Kohli'])
# plt.show()

df=pd.read_csv('batsman_season_record.csv')
print(df)
plt.bar(df['batsman'],df['2015'])
plt.show()

plt.bar(np.arange(df.shape[0]) - 0.2, df['2015'], width=0.2)
plt.bar(np.arange(df.shape[0]), df['2016'], width=0.2)
plt.bar(np.arange(df.shape[0]) + 0.2, df['2017'], width=0.2)

plt.xticks(np.arange(df.shape[0]), df['batsman'])
plt.xlabel('Batsman')
plt.ylabel('Runs')
plt.show()