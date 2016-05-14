import unittest
from statusjira import projectxml as prj
from statusjira import jiraticket as jt

class TestProjectXML(unittest.TestCase):

    def setUp(self):
        self.__testFile1 = "test/JiraProjectTestData.xml"
        self.__numtkts1  = 3

        self.projectFile = prj.file()

    def test_load (self):
        self.projectFile.load (self.__testFile1)

        self.assertEquals (self.__testFile1, self.projectFile.fileName())

    def test_isLoaded(self):
        self.assertFalse(self.projectFile.fileName())  #Empty string resolves to false
        self.projectFile.load (self.__testFile1)       #Load a project file
        self.assertTrue(self.projectFile.fileName())   #Non-Empty string resolves to true

    def test_findfirstticket(self):
        self.projectFile.load (self.__testFile1)       #Load a project file
        tkt = self.projectFile.findfirstticket()
        self.assertEquals("item", tkt.tag)

    def test_findticketnumber(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        ticketnumber = self.projectFile.findticketnumber(tkt)
        self.assertTrue(ticketnumber) #Verify that the ticket number string is not empty

    def test_findticketsummary(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        ticketsummary = self.projectFile.findticketsummary(tkt)
        self.assertTrue(ticketsummary)  #Verify that the ticket summary string is not empty

    def test_findticketstatus(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        ticketstatus = self.projectFile.findticketstatus(tkt)
        self.assertNotEqual(jt.const._unknown, ticketstatus)


    def test_findalltickets(self):        
        self.projectFile.load (self.__testFile1)       #Load a project file
        listoftickets = self.projectFile.findalltickets();
        self.assertEquals(self.__numtkts1, len(listoftickets)) 

        print listoftickets

if __name__ == '__main__':
    unittest.main()
