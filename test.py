
from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #check for html response 200
    def test_home(self):
        tester = webapp.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_content(self):
        tester = webapp.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        


    # check if content is html
    def test_home_content(self):
        tester = webapp.test_client(self)
        response = tester.get("/home")
        self.assertRegex(response.content_type, "html")

    # check returned data
    def test_home_data(self):
        tester = webapp.test_client(self)
        response = tester.get("/home")

    def test_add_content(self):
        tester = webapp.test_client(self)
        response = tester.get("/add")
        self.assertTrue(b'Name of Site' in response.data)
        self.assertTrue(b'URL of Site' in response.data)
        self.assertTrue(b'Editors First Name' in response.data)
        self.assertTrue(b'Editors Surname' in response.data)
        self.assertTrue(b'Editors Date Started' in response.data)            

if __name__ == "__main__":
    unittest.main()
