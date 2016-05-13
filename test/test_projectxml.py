import unittest
import os
from statusjira import projectxml as prj

class TestProjectXML(unittest.TestCase):

    def setUp(self):
        self.__testFile1 = "test/JiraProjectTestData.xml"

        self.projectFile = prj.file()

    def test_load (self):
        self.projectFile.load (self.__testFile1)

        self.assertEquals (self.__testFile1, self.projectFile.fileName())

    def test_isLoaded(self):
        self.assertFalse(self.projectFile.fileName())  #Empty string resolves to false
        self.projectFile.load (self.__testFile1)       #Load a project file
        self.assertTrue(self.projectFile.fileName())   #Non-Empty string resolves to true

    def test_tmp(self):        
        self.projectFile.load (self.__testFile1)       #Load a project file

        self.projectFile.tmp();
        

if __name__ == '__main__':
    unittest.main()
