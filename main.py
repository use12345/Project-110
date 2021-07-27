import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("population mean : - ", population_mean)
print(" std_deviation : - ", std_deviation)

dataset = []
for i in range(0,30) : 
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)

print("mean of sample: ",mean)
print("std_deviation of sample: ",std_deviation)





fig = ff.create_distplot([data],["temp"], show_hist=False)
fig.show()
