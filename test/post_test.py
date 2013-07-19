#!/usr/bin/env python
# coding: utf-8

#**********************************
# author:   h3idan
# datetime: 2013-07-16 14:07
#**********************************


import unittest
import server 

class TestPostView(unitest.TestCase):
    def setUp(self):
        self.apps = server.apps.test_client()

    def tearDown(self):
        pass

    def test_post(self):
        response = self.apps.get('/')
        assert(response.status_code==200)

if __name__ == '__main__':
    unittest.main()
