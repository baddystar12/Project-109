import csv 
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("blah.csv")
reading_list = df['reading score'].to_list()

mean = statistics.mean(reading_list)
median = statistics.median(reading_list)
mode = statistics.mode(reading_list)
std_dev = statistics.stdev(reading_list)

first_std_start, first_std_end = mean - std_dev, mean + std_dev
second_std_start, second_std_end = mean - (2* std_dev), mean + (2* std_dev)

list_of_data_1 = [result for result in reading_list if result > first_std_start and result < first_std_end]
list_of_data_2 = [result for result in reading_list if result > second_std_start and result < second_std_end]

print("mean = ", mean)
print("median = " , median)
print("mode = ", mode)
print("standard deviation = ", std_dev)
print("{}% of data lies between first quartile".format(len(list_of_data_1)*100.0/len(reading_list)))
print("{}% of data lies between second quartile".format(len(list_of_data_2)*100.0/len(reading_list)))

fig = ff.create_distplot([reading_list], ["result"], show_hist = False, colors = ['#5900b3'])
fig.show()