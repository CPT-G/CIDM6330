import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
from operator import itemgetter

path = "C:/Users/jpgan/OneDrive/Desktop/WTAMU/03.Spring_2024/6330 Software Eng and Systems Dev/CIDM6330_Assignments/CIDM6330/EM Planning Project/tl_2023_us_state/tl_2023_us_state.shp"
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
