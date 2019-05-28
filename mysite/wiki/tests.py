from django.test import TestCase
from django.urls import reverse
from wiki.models import Page

class Test1(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pages are available")#this is testing to check that there is a syste in place if there is no page.

class Test2(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "Wiki index") # This is making sure that there is a titl on the page.

class Test3(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "login")# this is test to see if there a login button

class Test4(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "logout") # this is testing to make sure that there is a logout button for the user

class Test5(TestCase):
    def testreplay(self):
        response = self.client.get(reverse('wiki:upload/'))
        self.assertContains(response, "No uploaded files") # this is testing to make sure that there is a logout button for the user











