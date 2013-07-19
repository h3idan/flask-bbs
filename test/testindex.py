
import os
import unittest
import server

class IndexTestCase(unittest.TestCase):
    
    def setUp(self):
        """ init """
        self.apps = server.apps.test_client()

    def tearDown(self):
        """ after compeleted """
        pass

    def test_index(self):
        response = self.apps.get('/index/')
        assert(response.status_code == 200)

if __name__ == "__main__":
    unittest.main()


