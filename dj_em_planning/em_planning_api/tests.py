from django.test import TestCase
import pandas as pd
import numpy as np
from matplotlib.testing.decorators import image_comparison
from em_planning_api.models import _get_hex_color
from em_planning_api.models import FakePlotting
from em_planning_api.models import LatLongPoints
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class UserTest(APITestCase):
    consumers_url = reverse("consumer")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        # self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_consumers_authenticated(self):
        response = self.client.get(self.consumers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_consumers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEquals(response.status_code, 401)

    def test_post_consumer_authenticated(self):
        data = {
            "user": "Magneto",
            "title": "Mr",
            "first_name": "Max",
            "last_name": "Eisenhardt",
            "organization": "Brotherhood of Mutants"
        }
        response = self.client.post(self.consumers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 8)


class EMDataTest(TestCase):
    """Ensure we can create a new EM Data object"""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.em_data = EMData.objects.create(
            frequency=32.345,
            device='FM',
            location='14SKD',
            grid_1=33819,
            grid_2=74840,
            lat=34.981177,
            long=-101.915893,
            nearhit='true')

    self.list_frequency

    def setUp(self):
        EMData.objects.create(
            frequency=32.345, device='FM', location='14SKD', grid_1=33819, grid_2=74840, lat=34.981177, long=-101.915893, nearhit='true'
        )
        EMData.objects.create(
            frequency=30.125, device='FM', location='14SKD', grid_1=33909, grid_2=79924, lat=34.981959, long=-101.914928, nearhit='false'
        )

    def test_lat_long(self):
        old_main = EMData.objects.get(lat=34.981177, long=-101.915893)
        kilgore_rc = EMData.objects.get(lat=34.981959, long=-101.914928)
        self.assertEqual(old_main.get_point(), 34.981177, -101.915893)
        self.assertEqual(kilgore_rc.get_point(), 34.981959, -101.914928)


class LatLongPointsTest(TestCase):
    """Scatterplot of x and y points"""
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

    def assert_plot_figures_added():
        num_figures_before = plt.scatter().number

        plt.scatter(latitudes_fm, longitudes_fm,
                    color='red', alpha=0.5, label="FM")
        plt.scatter(latitudes_tacsat, longitudes_tacsat,
                    color='blue', alpha=0.5, label="TACSAT")
        plt.scatter(latitudes_jcr, longitudes_jcr,
                    color='green', alpha=0.5, label="JCR")
        plt.scatter(latitudes_wifi, longitudes_wifi,
                    color='purple', alpha=0.5, label="WiFi")
        yield
        num_figures_after = plt.scatter().number
        assert num_figures_before < num_figures_after

    with assert_plot_figures_added():
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.legend(loc="upper left")
        plt.title('EM Emissions')
        plt.show()


class ColorTest(TestCase):
    def setUp(self):
        self.longMessage = True

    def test_get_hex_color(self):
        # Test valid hex colors:
        VALID_HEX_COLORS = [
            '#000000',
            '#FFCC00',
            '#ae44BB'
        ]

        for color in VALID_HEX_COLORS:
            self.assertEqual(_get_hex_color(color), color.upper(
            ), "'%s' should be formatted as uppercase" % color)

        # Test valid aliases of red:
        for color in ['r', 'red', '#FF0000']:
            self.assertEqual(_get_hex_color(color), '#FF0000',
                             "'%s' should be a valid alias for 'red'" % color)

        # Test invalid colors:
        INVALID_COLORS = [
            '#FC0',
            '#GFCC00',
            '#0000000',
            '11ee22',
            'colorthatdoesntexist',
            '#abc'
        ]

        for color in INVALID_COLORS:
            with self.assertRaises(ValueError):
                _get_hex_color(color)
                self.fail("'%s' should be an invalid color" % color)

        # Test invalid types:
        INVALID_TYPES = [
            [],
            {},
            123
        ]

        for color in INVALID_TYPES:
            with self.assertRaises(TypeError):
                _get_hex_color(color)
                self.fail("'%s' should be an invalid type" % color)


class FrequencyDeviceTest(TestCase):
    def test_frequency(self):
        freq = EMData.objects.get(frequency=32.345)
        self.assertEqual(freq.get_frequency(), 32.345)


class DataConversionTest(TestCase):
    def test_filtering(self):
        pass

    def test_aggregation(self):
        pass

    def test_dataframe_dtypes():
        df1 = pd.read_csv(em_data_mapping.csv)

        assert df1.dtypes['column1'] == int
        assert df1.dtypes['column2'] == object


class DateTimeTest(TestCase):


class FakePlottingTest(TestCase):

    def test_plot_square1():
        x, y = [0, 1, 2], [0, 1, 2]
        line, = plot_square(x, y)
        x_plot, y_plot = line.get_xydata().T
        np.assert_array_equal(y_plot, np.square(y))

    def test_module(mock_plt):
        x = np.arange(0, 5, 0.1)
        y = np.sin(x)
        my_module.plot_data(x, y, "my title")


class MappingTest(TestCase):
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

    def assert_plot_figures_added_map():
        num_figures_before_map = plt.geo_df().number
        yield
        num_figures_after_map = plt.geo_df().number
        assert num_figures_before_map < num_figures_after_map

    with assert_plot_figures_added_map():
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('EM Emissions')
        plt.show()


class LayoutTest(TestCase):
    @image_comparison(baseline_images=['spines_axes_positions'])
    def test_spines_axes_positions():
        fig = plt.figure()
        x = np.linspace(0, 2*np.pi, 100)
        y = 2*np.sin(x)
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('centered spines')
        ax.plot(x, y)
        ax.spines['right'].set_position(('axes', 0.1))
        ax.yaxis.set_ticks_position('right')
        ax.spines['top'].set_position(('axes', 0.25))
        ax.xaxis.set_ticks_position('top')
        ax.spines['left'].set_color('none')
        ax.spines['bottom'].set_color('none')
