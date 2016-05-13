import unittest
from statusjira import projectxml as prj

class TestProjectXML(unittest.TestCase):

    def setUp(self):
        self.__testFile1 = "JiraProjectTestData.xml"

        self.projectFile = prj.file()

    def test_load (self):
        self.projectFile.load (self.__testFile1)

        self.assertEquals (self.__testFile1, self.projectFile.fileName())

if __name__ == '__main__':
    unittest.main()
