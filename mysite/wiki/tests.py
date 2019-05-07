
from django.test import TestCase

import datetime

from django.urls import reverse

from django.test import TestCase

from django.utils import timezone


# Create your tests here.
class test(TestCase):
    
    def test_no_questions(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "No pages are available")

class test1(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "Wiki index")

