import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("em_data_no_mapping.csv")

latitudes = dataset.loc[:, 'Lat']
longitudes = dataset.loc[:, "Long"]

min_latitude = latitudes.min()
max_latitude = latitudes.max()
min_longitude = longitudes.min()
max_longitude = longitudes.max()

latitudes_fm = dataset.loc[:, 'Lat_FM']
longitudes_fm = dataset.loc[:, "Long_FM"]
latitudes_tacsat = dataset.loc[:, 'Lat_TACSAT']
longitudes_tacsat = dataset.loc[:, "Long_TACSAT"]
latitudes_jcr = dataset.loc[:, 'Lat_JCR']
longitudes_jcr = dataset.loc[:, "Long_JCR"]
latitudes_wifi = dataset.loc[:, 'Lat_WiFi']
longitudes_wifi = dataset.loc[:, "Long_WiFi"]


plt.scatter(latitudes_fm, longitudes_fm,
            color='red', alpha=0.5, label="FM")
plt.scatter(latitudes_tacsat, longitudes_tacsat,
            color='blue', alpha=0.5, label="TACSAT")
plt.scatter(latitudes_jcr, longitudes_jcr,
            color='green', alpha=0.5, label="JCR")
plt.scatter(latitudes_wifi, longitudes_wifi,
            color='purple', alpha=0.5, label="WiFi")


plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc="upper left")
plt.title('EM Emissions')
plt.show()
