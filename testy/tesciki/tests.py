from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class AddNumbersViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test1(self):
        num1 = 2
        num2 = 2
        self.assertEqual( num1, num2)
        return num1
    
    def test2(self):
        num1 = 2
        num2 = 3
        self.assertEqual( num1, num2)
        return num1
        
        
