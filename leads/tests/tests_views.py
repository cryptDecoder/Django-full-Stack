from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class HomePageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'landing.html')
