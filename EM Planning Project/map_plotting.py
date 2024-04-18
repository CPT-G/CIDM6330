import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets
import plotly.express as px
import pandas as pd
# import csv

"""with open("em_data.csv") as em_data_csv:
    reader = csv.reader(em_data_csv)
    for row in reader:
        print(row)"""


df_em_data = pd.read_csv("em_data.csv")
# print(df_em_data.to_string())

# use geopandas to convert lat and long to points
df_geo = gpd.GeoDataFrame(
    df_em_data, geometry=gpd.points_from_xy(df_em_data.longitude, df_em_data.latitude))

# get built in dataset from geopandas
world_data = gpd.read_file(gpd.dataset.get_path("naturalearth_lowres"))
# plot world map
axis = world_data[world_data.continent == "Louisiana"].plot(
    color="lightblue", edgecolor="black")

df_geo.plot(ax=axis, color="black")
plt.title("EM Data Points")

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(9, 6)
fig.savefig("matplot.png", dpi=200)
plt.show()

f = px.choropleth(df_em_data, locationmode="country names",
                  locations=df_em_data['country'], scope='louisiana', color=df_em_data['country'])
f.show()
