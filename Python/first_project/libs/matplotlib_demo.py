import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Example 1
year = [10, 20, 30, 40]
pop = [2.6, 3.5, 7.0, 8.1]
plt.scatter(year, pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Global population over years")
plt.yticks([0, 2, 4, 6, 8, 10], ["0B","2B","4B","6B","8B","10B"])

plt.show()
plt.close()


#Example 2
scores = [2,19,100,37,0,78,69,54,88,92,33, 11,23]
scores = sorted(scores)
plt.hist(scores, bins = 10)
plt.show()
plt.close()


#Example 3 - subplots

# Prepare data using Pandas
temps = [16.2, 18.3, 21.1, 24.9, 27.2, 28.9, 28.7, 27.9, 26.8, 24.7, 21.2, 17.2]
precipitations = [47,37,61,109,242,236,272,310,225,122,62,37]
months = [1,2,3,4,5,6,7,8,9,10,11,12]

weather = np.array([temps, precipitations, months])

df_weather = pd.DataFrame(weather
                        , index = ['TEMP', 'PRECIPITATION','MONTH']
                        , columns = [1,2,3,4,5,6,7,8,9,10,11,12])

# Draw                    
fig, ax = plt.subplots(2,1, sharex=True)

ax[0].plot(df_weather.loc['MONTH',:], df_weather.loc['TEMP',:], marker='o', color='r', linestyle='--')
ax[0].set_xlabel("Months")
ax[0].set_ylabel("Temperature (C)")

ax[1].plot(df_weather.loc['MONTH',:], df_weather.loc['PRECIPITATION',:], marker='v', color='b',linestyle='--')
ax[1].set_xlabel("Months")
ax[1].set_ylabel("Precipitation (mm)")

plt.show()
plt.close()





