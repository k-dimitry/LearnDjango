from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def setUp(self):
        """Initialization before each test"""

    def test_mainpage(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertIn('women/index.html', response.template_name)
        self.assertTemplateUsed(response, 'women/index.html')
        self.assertEqual(response.context_data['title'], 'Main Page')

    def text_redirect_addpage(self):
        path = reverse('add_page')
        redirect_uri = reverse('users:login') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)

    def text_case_2(self):
        pass

    def tearDown(self):
        """Actions after each test"""
