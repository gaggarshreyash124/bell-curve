import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as pf

df = pd.read_csv("h,w.csv")
fig = pf.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist = False)

fig.show()

