from em_planning_arch.domain.model import DomainEMData
from django.db import models
from django.contrib.auth import get_user_model
# from django.utils import timezone (not assessed)
import matplotlib.pyplot as plt
import csv
import json
import numpy as np
import pandas as pd
# import geopandas as gpd (not assessed)
from shapely.geometry import Point
import matplotlib.pyplot as plt


class User(models.User):
    """
    User Model
    Defines the attributes of User Info
    """
    user = get_user_model()
    title = models.CharField(max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    organization = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EMData(models.Model):
    """
    EM Data Model
    Defines the attributes of our EM Data
    """
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    frequency = models.IntegerField()
    device = models.CharField(max_length=6)
    location = models.CharField(max_length=5)
    grid_1 = models.IntegerField()
    grid_2 = models.IntegerField()
    lat = models.IntegerField()
    long = models.IntegerField()
    nearhit = models.BooleanField()
    FREQUENCY = (
        ('fm', 'FM'),
        ('tacsat', 'TACSAT'),
        ('jcr', 'JCR'),
        ('wifi', 'WiFi'),
    )

    def __str__(self):
        return f"{self.frequency}"

    class Meta:
        app_label = "em_planning_api"

    @staticmethod
    def update_from_domain(domain_em_data: DomainEMData):
        try:
            em_data = em_data.objects.get(frequency=domain_em_data.frequency)
        except em_data.DoesNotExist:
            em_data = em_data(frequency=domain_em_data.frequency)

        em_data.date = domain_em_data.date
        em_data.time = domain_em_data.time
        em_data.frequency = domain_em_data.frequency
        em_data.device = domain_em_data.device
        em_data.location = domain_em_data.location
        em_data.grid_1 = domain_em_data.grid_1
        em_data.grid_2 = domain_em_data.grid_2
        em_data.lat = domain_em_data.lat
        em_data.long = domain_em_data.long
        em_data.nearhit = domain_em_data.nearhit
        em_data.save()

    def to_domain(self) -> DomainEMData:
        b = DomainEMData(
            date=self.date,
            time=self.time,
            frequency=self.frequency,
            device=self.device,
            location=self.location,
            grid_1=self.grid_1,
            grid_2=self.grid_2,
            lat=self.lat,
            long=self.long,
            nearhit=self.nearhit,
        )
        return b


class LatLongPoints(models.Model):
    """
    Latitude and Longitude Points Model
    Defines the attributes of our Lat and Long Points
    x and y values converting to point for matplolib
    """

    dataset = pd.read_csv(
        "dj_em_planning/outside_scope/em_data_no_mapping.csv")

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

    def __str__(self):
        return f'{self.latitudes} {self.longitudes}'


class Colors(models.Model):
    """
    Color Model
    Defines the attributes of colors on scatterplot
    """
    _MATPLOTLIB_COLOR_MAP = {
        'b': 'blue',
        'g': 'green',
        'r': 'red',
        'c': 'cyan',
        'm': 'magenta',
        'y': 'yellow',
        'k': 'black',
        'w': 'white'
    }

    _HTML_COLOR_CODES = {
        'aliceblue':            '#F0F8FF',
        'antiquewhite':         '#FAEBD7',
        'aqua':                 '#00FFFF',
        'aquamarine':           '#7FFFD4',
        'azure':                '#F0FFFF',
        'beige':                '#F5F5DC',
        'bisque':               '#FFE4C4',
        'black':                '#000000',
        'blanchedalmond':       '#FFEBCD',
        'blue':                 '#0000FF',
        'blueviolet':           '#8A2BE2',
        'brown':                '#A52A2A',
        'burlywood':            '#DEB887',
        'cadetblue':            '#5F9EA0',
        'chartreuse':           '#7FFF00',
        'chocolate':            '#D2691E',
        'coral':                '#FF7F50',
        'cornflowerblue':       '#6495ED',
        'cornsilk':             '#FFF8DC',
        'crimson':              '#DC143C',
        'cyan':                 '#00FFFF',
        'darkblue':             '#00008B',
        'darkcyan':             '#008B8B',
        'darkgoldenrod':        '#B8860B',
        'darkgray':             '#A9A9A9',
        'darkgreen':            '#006400',
        'darkgrey':             '#A9A9A9',
        'darkkhaki':            '#BDB76B',
        'darkmagenta':          '#8B008B',
        'darkolivegreen':       '#556B2F',
        'darkorange':           '#FF8C00',
        'darkorchid':           '#9932CC',
        'darkred':              '#8B0000',
        'darksalmon':           '#E9967A',
        'darkseagreen':         '#8FBC8F',
        'darkslateblue':        '#483D8B',
        'darkslategray':        '#2F4F4F',
        'darkslategrey':        '#2F4F4F',
        'darkturquoise':        '#00CED1',
        'darkviolet':           '#9400D3',
        'deeppink':             '#FF1493',
        'deepskyblue':          '#00BFFF',
        'dimgray':              '#696969',
        'dimgrey':              '#696969',
        'dodgerblue':           '#1E90FF',
        'firebrick':            '#B22222',
        'floralwhite':          '#FFFAF0',
        'forestgreen':          '#228B22',
        'fuchsia':              '#FF00FF',
        'gainsboro':            '#DCDCDC',
        'ghostwhite':           '#F8F8FF',
        'gold':                 '#FFD700',
        'goldenrod':            '#DAA520',
        'gray':                 '#808080',
        'green':                '#008000',
        'greenyellow':          '#ADFF2F',
        'grey':                 '#808080',
        'honeydew':             '#F0FFF0',
        'hotpink':              '#FF69B4',
        'indianred':            '#CD5C5C',
        'indigo':               '#4B0082',
        'ivory':                '#FFFFF0',
        'khaki':                '#F0E68C',
        'lavender':             '#E6E6FA',
        'lavenderblush':        '#FFF0F5',
        'lawngreen':            '#7CFC00',
        'lemonchiffon':         '#FFFACD',
        'lightblue':            '#ADD8E6',
        'lightcoral':           '#F08080',
        'lightcyan':            '#E0FFFF',
        'lightgoldenrodyellow': '#FAFAD2',
        'lightgray':            '#D3D3D3',
        'lightgreen':           '#90EE90',
        'lightgrey':            '#D3D3D3',
        'lightpink':            '#FFB6C1',
        'lightsalmon':          '#FFA07A',
        'lightseagreen':        '#20B2AA',
        'lightskyblue':         '#87CEFA',
        'lightslategray':       '#778899',
        'lightslategrey':       '#778899',
        'lightsteelblue':       '#B0C4DE',
        'lightyellow':          '#FFFFE0',
        'lime':                 '#00FF00',
        'limegreen':            '#32CD32',
        'linen':                '#FAF0E6',
        'magenta':              '#FF00FF',
        'maroon':               '#800000',
        'mediumaquamarine':     '#66CDAA',
        'mediumblue':           '#0000CD',
        'mediumorchid':         '#BA55D3',
        'mediumpurple':         '#9370DB',
        'mediumseagreen':       '#3CB371',
        'mediumslateblue':      '#7B68EE',
        'mediumspringgreen':    '#00FA9A',
        'mediumturquoise':      '#48D1CC',
        'mediumvioletred':      '#C71585',
        'midnightblue':         '#191970',
        'mintcream':            '#F5FFFA',
        'mistyrose':            '#FFE4E1',
        'moccasin':             '#FFE4B5',
        'navajowhite':          '#FFDEAD',
        'navy':                 '#000080',
        'oldlace':              '#FDF5E6',
        'olive':                '#808000',
        'olivedrab':            '#6B8E23',
        'orange':               '#FFA500',
        'orangered':            '#FF4500',
        'orchid':               '#DA70D6',
        'palegoldenrod':        '#EEE8AA',
        'palegreen':            '#98FB98',
        'paleturquoise':        '#AFEEEE',
        'palevioletred':        '#DB7093',
        'papayawhip':           '#FFEFD5',
        'peachpuff':            '#FFDAB9',
        'peru':                 '#CD853F',
        'pink':                 '#FFC0CB',
        'plum':                 '#DDA0DD',
        'powderblue':           '#B0E0E6',
        'purple':               '#800080',
        'rebeccapurple':        '#663399',
        'red':                  '#FF0000',
        'rosybrown':            '#BC8F8F',
        'royalblue':            '#4169E1',
        'saddlebrown':          '#8B4513',
        'salmon':               '#FA8072',
        'sandybrown':           '#F4A460',
        'seagreen':             '#2E8B57',
        'seashell':             '#FFF5EE',
        'sienna':               '#A0522D',
        'silver':               '#C0C0C0',
        'skyblue':              '#87CEEB',
        'slateblue':            '#6A5ACD',
        'slategray':            '#708090',
        'slategrey':            '#708090',
        'snow':                 '#FFFAFA',
        'springgreen':          '#00FF7F',
        'steelblue':            '#4682B4',
        'tan':                  '#D2B48C',
        'teal':                 '#008080',
        'thistle':              '#D8BFD8',
        'tomato':               '#FF6347',
        'turquoise':            '#40E0D0',
        'violet':               '#EE82EE',
        'wheat':                '#F5DEB3',
        'white':                '#FFFFFF',
        'whitesmoke':           '#F5F5F5',
        'yellow':               '#FFFF00',
        'yellowgreen':          '#9ACD32'
    }

    def _get_hex_color(self, color):
        """
        Return the hex color code for a given color.
        Args:
            color (str): Color of interest. Can be hex ('#00FFFF'), named ('cyan'), or matplotlib-like ('c').
        Returns:
        str: Hex color code for the given color.
        Raises:
            ValueError: If the color isn't supported.
        """
        if not re.match('^#[0-9a-fA-F]{6}$', color):
            color = _MATPLOTLIB_COLOR_MAP.get(color, color)

            if color not in _HTML_COLOR_CODES:
                raise ValueError("Color '%s' isn't supported!" % color)

            color = _HTML_COLOR_CODES[color]

        return color.upper()


class FrequencyDevice(models.Model):
    """
    Frequency by Device Model
    Defines the attributes of our Frequencies by Device
    Frequency Integer to String (Common naming) Conversion Model
    ID and change int to str: 4 types of device based on frequency parameters
    """
    frequency = models.IntegerField()
    FREQUENCY = (
        ('fm', 'FM'),
        ('tacsat', 'TACSAT'),
        ('jcr', 'JCR'),
        ('wifi', 'WiFi'),
    )

    def __init__(self, FM, TACSAT, JCR, WiFi):
        self.FM = FM
        self.TACSAT = TACSAT
        self.JCR = JCR
        self.WiFi = WiFi

    def int_to_freq_str(self):
        freq = self.to_str
        return freq

    def to_str(self, number):
        if (number >= 90):
            return ('FM')
        elif (225 < number <= 512):
            return ('TACSAT')
        elif (950 < number <= 2150):
            return ('JCR')
        elif (2150 < number):
            return ('WiFi')
        else:
            return ('Outside frequency parameters')


class DataConversion(models.Model):
    """
    CSV to JSON conversion Model
    Defines the attributes of our CSV and JSON Data
    """
    path_csv = ('em_planning_arch/domain/em_data.csv')
    path_json = ('dj_em_planning.db.em_data')

    def csv_to_json(self, path_csv, path_json):
        jsonArray = []

        with open(path_csv, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            for row in csvReader:
                jsonArray.append(row)

        with open(path_json, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)

    path_csv = r'data.csv'
    path_json = r'data.json'
    csv_to_json(path_csv, path_json)


class DateTime(models.Model):  # DateTimeField Testing likely unecessary
    """
    DateTimeField Model
    Defines the attributes of our DateTimeField
    Used to test if DateTimeField changes are detected properly
    """

    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

    def __str__(self):
        return self.timestamp.strftime('%Y-%m-%d')


class FakePlotting(models.Model):  # Experiment with matplotlib
    def plot_square(self, x, y):
        y_squared = np.square(y)
        return plt.plot(x, y_squared)

    def plot_data(self, x, y, title):
        plt.figure()
        plt.title(title)
        plt.plot(x, y)
        plt.show()


class Mapping(models.Model):
    """
    Mapping Model
    Defines the attributes of our plotting on maps or charts
    """
    dataset = pd.read_csv("dj_em_planning/outside_scope/em_data_mapping.csv")

    latitudes = dataset.loc[:, 'Lat']
    longitudes = dataset.loc[:, "Long"]

    min_latitude = latitudes.min()
    max_latitude = latitudes.max()
    min_longitude = longitudes.min()
    max_longitude = longitudes.max()

    data_points = [Point(xy) for xy in zip(longitudes, latitudes)]

    def __str__(self):
        return f'{self.latitudes} {self.longitudes}'


class Layout(models.Model):
    """
    Matplotlib Layout Model
    Defines the attributes of our Matplotlib plotting
    """

    def __init__(self, ax, fig, spines, xaxis, yaxis):
        self.ax = ax
        self.fig = fig
        self.spines = spines
        self.xaxis = xaxis
        self.yaxis = yaxis
