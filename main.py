import pandas as pd
import time

file = "data/iot.csv"

df = pd.read_csv(file, low_memory=False)


df['icon'] = df['icon'].astype("category")
df.info()

# firstly lets check for null values
print(f'rows = {df.shape[0] } columns = {df.shape[1]}')
# lets check for non null values
print(df.notnull().sum())
# for every category there are 503910 non nulls which means there is one null value,
# lets find out this null value
print(df.head())
print(df.tail())
# As we see the last row has NAN values, so lets remove them

df = df.dropna()

print(df.tail())

print(df.notnull().sum())

# now the data shape is consistent
# lets check the data types
df.info()

# there are few columns with categorical values, lets convert them into category type
df['icon'] = df['icon'].astype("category")
df['summary'] = df['summary'].astype("category")
df['cloudCover'] = df['cloudCover'].astype("category")

df.info()

# check category types
print(df['icon'].value_counts())
print(df['summary'].value_counts())
print(df['cloudCover'].value_counts())

# lets convert the time into readable format, currently its in unix format
# df['time'] = df['time'].astype('float')
df.info()

df.head()

import datetime

df['time'] = df.time.apply(lambda d: datetime.datetime.fromtimestamp(int(d)).strftime('%Y-%m-%d %H:%M:%S'))

df.info()

df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)

df = df.set_index("time")
import matplotlib.pyplot as plt
import os
if not os.path.exists("images"):
    os.mkdir("images")


def plot_df(parameter):
    plt.figure()
    df[parameter].plot()
    plt.show()
    plt.xlabel("Time")
    plt.ylabel(parameter)
    plt.title("Plot for " + parameter)
    plt.savefig("images/plot_"+parameter+".png")


import plotly.graph_objects as go


def plot_with_plotly(parameter="temperature"):
    fig = go.Figure()
    trace = go.Scatter(
        x=df.index,
        y=df[parameter],
        mode="lines",

    )

    fig.update_layout(
        title="Plot for "+parameter,
        xaxis_title="time",
        yaxis_title=parameter
    )
    fig.add_trace(trace)
    fig.write_image("images/plot_" + parameter + ".png")
    fig.show()


to_plot = ["temperature", "humidity", "visibility", "pressure", "windSpeed",
           "windBearing", "precipIntensity", "dewPoint"]
# to_plot = ["temperature"]

for feat in to_plot:
    # plot_df(feat)

    plot_with_plotly(feat)

