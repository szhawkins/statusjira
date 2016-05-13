import unittest
from statusjira import projectxml

class TestProjectXML(unittest.TestCase):

    def setUp(self):
        self.tmp = 1234

    def test_load (self):

        self.tmp = 5678

if __name__ == '__main__':
    unittest.main()
