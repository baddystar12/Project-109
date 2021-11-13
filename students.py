import csv 
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("blah.csv")
data = df['reading score'].to_list()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)

first_std_start, first_std_end = mean - std_dev, mean + std_dev
second_std_start, second_std_end = mean - (2* std_dev), mean + (2* std_dev)
third_std_start, third_std_end = mean - (3* std_dev), mean + (3* std_dev)

list_of_data_1 = [result for result in data if result > first_std_start and result < first_std_end]
list_of_data_2 = [result for result in data if result > second_std_start and result < second_std_end]
list_of_data_3 = [result for result in data if result > third_std_start and result < third_std_end]

print("mean = ", mean)
print("median = " , median)
print("mode = ", mode)
print("standard deviation = ", std_dev)
print("{}% of data lies between first quartile".format(len(list_of_data_1)*100.0/len(data)))
print("{}% of data lies between second quartile".format(len(list_of_data_2)*100.0/len(data)))
print("{}% of data lies between third quartile".format(len(list_of_data_3)*100.0/len(data)))

fig = ff.create_distplot([data], ["reading scores"], show_hist = False, colors = ['yellow'])
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0,17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="standard deviation 2"))
fig.show()
