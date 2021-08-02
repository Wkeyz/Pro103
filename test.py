import pandas as pd

import plotly.express as px

df = pd.read_csv("covid.csv")

fig = px.line(df, x="Cases", y="Country", color="Country", title="Cases Per Country")

fig.show()