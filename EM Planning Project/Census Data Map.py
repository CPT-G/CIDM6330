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
