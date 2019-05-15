from django.test import TestCase

from django.urls import reverse

from wiki.models import Page

class Test1(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pages are available")

class Test2(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "Wiki index")

class Test3(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "login")

class Test4(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "logout")







