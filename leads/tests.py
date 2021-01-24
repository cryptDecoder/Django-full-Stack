from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class HomePageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('home'))
        print(response.status_code)
