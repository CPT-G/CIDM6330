from django.test import TestCase
import pandas as pd

from em_planning_api.models import _get_hex_color


class UserTest(TestCase):


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


class MappingTest(TestCase):
    def get_point(self):
        return self.Lat + self.Long


class LayoutTest(TestCase):
