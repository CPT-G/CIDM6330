# from django.test import TestCase
# import pandas as pd

# from em_planning_api.color import _get_hex_color


# class ColorTest(TestCase):
#     def setUp(self):
#         self.longMessage = True

#     def test_get_hex_color(self):
#         # Test valid hex colors:
#         VALID_HEX_COLORS = [
#             '#000000',
#             '#FFCC00',
#             '#ae44BB'
#         ]

#         for color in VALID_HEX_COLORS:
#             self.assertEqual(_get_hex_color(color), color.upper(
#             ), "'%s' should be formatted as uppercase" % color)

#         # Test valid aliases of red:
#         for color in ['r', 'red', '#FF0000']:
#             self.assertEqual(_get_hex_color(color), '#FF0000',
#                              "'%s' should be a valid alias for 'red'" % color)

#         # Test invalid colors:
#         INVALID_COLORS = [
#             '#FC0',
#             '#GFCC00',
#             '#0000000',
#             '11ee22',
#             'colorthatdoesntexist',
#             '#abc'
#         ]

#         for color in INVALID_COLORS:
#             with self.assertRaises(ValueError):
#                 _get_hex_color(color)
#                 self.fail("'%s' should be an invalid color" % color)

#         # Test invalid types:
#         INVALID_TYPES = [
#             [],
#             {},
#             123
#         ]

#         for color in INVALID_TYPES:
#             with self.assertRaises(TypeError):
#                 _get_hex_color(color)
#                 self.fail("'%s' should be an invalid type" % color)


# class TestDataFrameOperations(TestCase):
#     def test_filtering(self):
#         pass

#     def test_aggregation(self):
#         pass

#     def test_dataframe_dtypes():
#         df1 = pd.read_csv(em_data_mapping.csv)

#         assert df1.dtypes['column1'] == int
#         assert df1.dtypes['column2'] == object

from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from em_planning_api.views import CustomerView
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ApiUrlsTests(SimpleTestCase):

    def test_get_customers_is_resolved(self):
        url = reverse('customer')
        self.assertEquals(resolve(url).func.view_class, CustomerView)


class CustomerAPIViewTests(APITestCase):
    customers_url = reverse("customer")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        # self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEquals(response.status_code, 401)

    def test_post_customer_authenticated(self):
        data = {
            "title": "Mr",
            "name": "Peter",
            "last_name": "Parkerz",
            "gender": "M",
            "status": "published"
        }
        response = self.client.post(self.customers_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 8)


class CustomerDetailAPIViewTests(APITestCase):
    customer_url = reverse('customer-detail', args=[1])
    customers_url = reverse("customer")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        # self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Saving customer
        data = {
            "title": "Mrs",
            "name": "Johnson",
            "last_name": "MOrisee",
            "gender": "F",
            "status": "published"
        }
        self.client.post(
            self.customers_url, data, format='json')

    def test_get_customer_autheticated(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Johnson')

    def test_get_customer_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_customer_authenticated(self):
        response = self.client.delete(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
