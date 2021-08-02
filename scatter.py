import pandas as pd

import plotly.express as px

df = pd.read_csv("covid.csv")
fig = px.scatter(df, x="cases", y="country",size = "Percentage",color="Country",size_max=60)
fig.show()