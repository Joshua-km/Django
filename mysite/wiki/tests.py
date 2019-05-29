from django.test import TestCase
from django.urls import reverse
from wiki.models import Page
from django.contrib.auth.models import User # This is import enables me to test the login & logout syteame

class Test1(TestCase):#This is testing to check that there is a syste in place if there is no page.
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pages are available")

class Test2(TestCase):# This is making sure that there is a title on the page.
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "Wiki index") 

class Test3(TestCase):# This is test to see if there a way that the user can login to the Wiki
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "login")

class Test4(TestCase):# This is test to see if there a way that the user can logout of the Wiki
    def testreplay(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "logout")



class Test5(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@mywiki.com', 'TestUserpassword')

    def testLogin(self):  #This is testing to make sure that the login works
        self.client.login(username='TestUser', password='TestUserpassword')
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "logout")

    def testLogout(self): #This is testing to make sure that the logout works
        self.client.logout()
        response = self.client.get(reverse('wiki:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username:")


class Test6(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

    def testreplay(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.get('/wiki/upload', follow=True)
        self.assertContains(response, "upload")

    def test_edit_page(self):
        self.client.login(username='TestUser', password='testingpassword')
        response = self.client.post('/wiki/editing/edit', follow=True)
        self.assertContains(response, 'editing')













