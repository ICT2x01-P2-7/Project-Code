import unittest
from app import connect

class testClass(unittest.TestCase):
    def test_connect(self):
        self.assertEqual(connect(), '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918')

# This test case test to make sure that the application returns an error when the instructor password is wrong
def test_connect_fail():
    app = connect()
    password = 'password'
    assert app.hexadecimal != '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'

# This test case test to make sure that the application sucessfully validates the instructor password
def test_connect_pass():
    app = connect()
    password = 'admin'
    assert app.hexadecimal == '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'