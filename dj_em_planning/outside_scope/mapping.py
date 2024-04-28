import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

dataset = pd.read_csv("em_data_mapping.csv")

latitudes = dataset.loc[:, 'Lat']
longitudes = dataset.loc[:, "Long"]

min_latitude = latitudes.min()
max_latitude = latitudes.max()
min_longitude = longitudes.min()
max_longitude = longitudes.max()

data_points = [Point(xy) for xy in zip(longitudes, latitudes)]


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(color='grey', figsize=(16, 11))


geo_df = gpd.GeoDataFrame(
    dataset, crs={'init': 'epsg:4326'}, geometry=data_points)
geo_df.plot(markersize=10, color='red', ax=ax)

ax.axis('on')
ax.set_xlim(min_longitude - 0.003, max_longitude + 0.003)
ax.set_ylim(min_latitude - 0.003, max_latitude + 0.003)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('EM Emissions')
plt.show()
