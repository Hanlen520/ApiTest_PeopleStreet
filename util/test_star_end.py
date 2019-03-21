import unittest
from util.selse_feng import CreateDriver
from util import log


class TestStarEnd(unittest.TestCase):
    '''
    unittest 公共的setUp 与tearDowm
    '''

    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

