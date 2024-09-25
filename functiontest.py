import unittest
import json
from flask import Flask
from api_code.api_app import api_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Setup method to initialize the test client."""
        self.tester = api_app.test_client(self)

    def test_true_when_x_is_17(self):
        response = self.tester.get('/is_prime/17')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', response.get_json())
        self.assertTrue(response.get_json()['Is_prime'])
        print(f"Test(/is_prime/17) ==> Response: {response.data.decode('utf-8')}")

    def test_true_when_x_is_13219(self):
        response = self.tester.get('/is_prime/13219')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', response.get_json())
        self.assertTrue(response.get_json()['Is_prime'])
        print(f"Test(/is_prime/13219) ==> Response: {response.data.decode('utf-8')}")

    def test_false_when_x_is_36(self):
        response = self.tester.get('/is_prime/36')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', response.get_json())
        self.assertFalse(response.get_json()['Is_prime'])
        print(f"Test(/is_prime/36) ==> Response: {response.data.decode('utf-8')}")

if __name__ == '__main__':
    unittest.main()
