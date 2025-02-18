# Attempt 1
"""
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets
import plotly.express as px
import pandas as pd
# import csv

with open("em_data.csv") as em_data_csv:
    reader = csv.reader(em_data_csv)
    for row in reader:
        print(row)


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
"""


# Attempt 2
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import contextily as ctx
import geopandas as gpd
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable

# %%
path = "C:/Users/jpgan/OneDrive/Desktop/WTAMU/03.Spring_2024/6330 Software Eng and Systems Dev/CIDM6330_Assignments/CIDM6330/EM Planning Project/tl_2023_us_state/tl_2023_us_state.shp"
df = gpd.read_file(path)
df = df.to_crs("EPSG:4326")

# Information for each state
df.iloc[0, :]
df.plot()
non_continental = ['HI', 'VI', 'MP', 'GU', 'AK', 'AS', 'PR']
us49 = df
for n in non_continental:
    us49 = us49[us49.STUSPS != n]

us49.boundary.plot()
plt.show()

f, ax = plt.subplots(1, 1, figsize=(8, 6), sharex=True, sharey=True, dpi=300)
plt.title('Simple Map of US States')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0, alpha=0.5)
us49.plot('ALAND', ax=ax, alpha=0.5, cmap='Pastel1',
          edgecolor='k', legend=True, cax=cax, linewidth=0.1)
plt.show()

us49['ALAND_miles'] = us49['ALAND']*3.86102e-7
us49['AWATER_miles'] = us49['AWATER']*3.86102e-7
us49['centroid'] = us49.centroid

f, ax = plt.subplots(1, 1, figsize=(8, 6), sharex=True, sharey=True, dpi=300)
plt.title('Map of US States with Centroids')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0, alpha=0.5)
us49.plot('ALAND_miles', ax=ax, alpha=0.5, cmap='Pastel1', edgecolor='k',
          legend=True, cax=cax, linewidth=0.1, label='Inline label')
plt.ylabel('Square miles', fontsize=6)
us49['centroid'].plot(ax=ax, marker='o', color='red', markersize=5)
plt.show()


def StatesPlot(df, data, cmap):
    f, ax = plt.subplots(1, 1, figsize=(15, 10),
                         sharex=True, sharey=True, dpi=300)
    f.tight_layout()
    plt.title('United States Map - Variable = ' + data)
    ax.set_axis_off()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%",
                              pad=0.5, alpha=0.5)
    df.plot(data, ax=ax, alpha=0.5, cmap=cmap,
            edgecolor='k', legend=True, cax=cax, linewidth=0.1)
    plt.ylabel('Square miles', fontsize=12)
    plt.show()


StatesPlot(us49, 'ALAND_miles', 'summer')


data = 'ALAND_miles'
cmap = 'Spectral'
zoom = 5
dpi = 100

# w,s,e,n = states.total_bounds

us49.crs = "EPSG:4326"

f, ax = plt.subplots(1, 1, figsize=(20, 12), sharex=True, sharey=True, dpi=dpi)
f.tight_layout(pad=0.8)
ax.set_axis_off()
plt.title('US Map using Contextily', fontsize='large')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.2)
ux = us49.to_crs(epsg=3857).plot(data, ax=ax, edgecolor='k',
                                 cmap=cmap, alpha=0.2, legend=True, cax=cax)
ctx.add_basemap(ux, zoom=zoom, source=ctx.providers.OpenStreetMap.Mapnik)
plt.ylabel('Million square miles', fontsize=12)
# Use savefig to save your map
plt.savefig('US Contextily Map with zoom = ' + str(zoom) + ' .png')
plt.show()

ctx.providers.keys()

# list of states using STUSPS
us49['STUSPS'].unique()


def statePlot(st, data, cmap, zoom, dpi):
    state = us49.loc[us49['STUSPS'] == st]
    state.crs = "EPSG:4326"
    f, ax = plt.subplots(1, 1, figsize=(8, 8),
                         sharex=True, sharey=True, dpi=dpi)
    f.tight_layout(pad=0.8)
    ax.set_axis_off()
    plt.title('Map using Contextily - ' + data, fontsize='large')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%", pad=0.2)
    ux = state.to_crs(epsg=3857).plot(data, ax=ax,
                                      edgecolor='blue',    cmap=cmap, alpha=0.2,
                                      legend=True, cax=cax)
    ctx.add_basemap(ux,    zoom=zoom,
                    source=ctx.providers.OpenStreetMap.Mapnik)
    plt.ylabel('Million square miles', fontsize=12)
    # Use savefig to save your map
    plt.savefig(
        'US Contextily Map with zoom = ' + str(zoom) + ' .png')
    plt.show()


statePlot('LA', 'ALAND_miles', 'summer', 5, 200)

statePlot('LA', 'ALAND_miles', 'summer', 9, 300)
"""


# Attempt 3
"""
from operator import itemgetter
from geopandas import GeoDataFrame
from shapely.geometry import Point


path = "C:/Users/jpgan/OneDrive/Desktop/WTAMU/00.Code/MSCISBA/CIDM6330/final_project/gov_mapping_data/tl_2023_us_state/tl_2023_us_state.shp"
df = gpd.read_file(path)

fig, ax = plt.subplots(figsize=(16, 11))
df.plot(ax=ax, alpha=0.4, color='grey')
ax.set_ylim(30.5, 31.5)
ax.set_xlim(-92, -93.5)
ax.set_yticks([30.5, 30.6, 30.7, 30.8, 30.9, 31, 31.1,
              31.2, 31.3, 31.4, 31.5], minor=False)
ax.set_xticks([-92, -92.1, -92.2, -92.3, -92.4, -92.5, -92.6, -92.7, -
              92.8, -92.9, -93, -93.1, -93.2, -93.3, -93.4, -93.5], minor=False)
ax.yaxis.grid(True, which='major')
ax.xaxis.grid(True, which='major')

em = pd.read_csv("em_data.csv", delimiter=',', skiprows=0, low_memory=False)
crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(em['Lat'], em['Long'])]

geo_df = gpd.GeoDataFrame(em, crs=crs, geometry=geometry)
geo_df.head()

geo_df.plot(ax=ax, markersize=20, color='blue',
            marker='o', label='Emission')
plt.legend()
plt.show()
"""


# Attempt 4
"""
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib import cm


dataset = pd.read_csv("em_data_test.csv")

latitudes_fm = dataset.loc[:, 'Lat_FM']
longitudes_fm = dataset.loc[:, "Long_FM"]
latitudes_tacsat = dataset.loc[:, 'Lat_TACSAT']
longitudes_tacsat = dataset.loc[:, "Long_TACSAT"]
latitudes_jcr = dataset.loc[:, 'Lat_JCR']
longitudes_jcr = dataset.loc[:, "Long_JCR"]
latitudes_wifi = dataset.loc[:, 'Lat_WiFi']
longitudes_wifi = dataset.loc[:, "Long_WiFi"]


min_latitude = latitudes_fm.min()
max_latitude = latitudes_fm.max()
min_longitude = longitudes_fm.min()
max_longitude = longitudes_fm.max()

data_points_fm = [Point(xy) for xy in zip(longitudes_fm, latitudes_fm)]
data_points_tacsat = [Point(xy)
                      for xy in zip(longitudes_tacsat, latitudes_tacsat)]
data_points_jcr = [Point(xy) for xy in zip(longitudes_jcr, latitudes_jcr)]
data_points_wifi = [Point(xy) for xy in zip(longitudes_wifi, latitudes_wifi)]


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(color='grey', figsize=(16, 11))


geo_df = gpd.GeoDataFrame(
    dataset, crs={'init': 'epsg:4326'}, geometry=data_points_fm)
geo_df.plot(markersize=10, color='red', ax=ax)
geo_df = gpd.GeoDataFrame(
    dataset, crs={'init': 'epsg:4326'}, geometry=data_points_tacsat)
geo_df.plot(markersize=10, color='blue', ax=ax)
geo_df = gpd.GeoDataFrame(
    dataset, crs={'init': 'epsg:4326'}, geometry=data_points_jcr)
geo_df.plot(markersize=10, color='green', ax=ax)
geo_df = gpd.GeoDataFrame(
    dataset, crs={'init': 'epsg:4326'}, geometry=data_points_wifi)
geo_df.plot(markersize=10, color='purple', ax=ax)

ax.axis('on')
ax.set_xlim(min_longitude - 0.003, max_longitude + 0.003)
ax.set_ylim(min_latitude - 0.003, max_latitude + 0.003)


plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('EM Emissions')
plt.show()
"""
