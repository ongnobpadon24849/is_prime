import unittest
import json
from flask import Flask
from api_code.api_app import api_app

print("Testing the API...")
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = api_app.test_client()

    def test_true_when_x_is_17(self):
        response = self.tester.get('/is_prime/17')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', data)
        self.assertEqual(data.get('Is_prime'), True)
        print(f"Test(/is_prime/17) ==> Response: {data}")

    def test_true_when_x_is_13219(self):
        response = self.tester.get('/is_prime/13219')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', data)
        self.assertEqual(data.get('Is_prime'), True)
        print(f"Test(/is_prime/13219) ==> Response: {data}")

    def test_false_when_x_is_36(self):
        response = self.tester.get('/is_prime/36')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Is_prime', data)
        self.assertEqual(data.get('Is_prime'), False)
        print(f"Test(/is_prime/36) ==> Response: {data}")
        

if __name__ == '__main__':
    unittest.main()
