import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df= mean_list
    mean = statistics.mean(df)
    fig= ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list =[]
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)

    print("Mean of Sampling Distribution: ", mean)
    print("Standard deviation of Sampling Distribution is : ", std_deviation)
setup()


population_mean = statistics.mean(data)
print("population mean : - ", population_mean)
std_deviation = statistics.stdev(data)
print(" std_deviation : - ", std_deviation)


