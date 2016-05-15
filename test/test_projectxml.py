import unittest
from statusjira import projectxml as prj
from statusjira import appglobal as AG

class TestProjectXML(unittest.TestCase):

    def setUp(self):
        self.__testFile1 = "test/JiraProjectTestData.xml"
        self.__numtkts1  = 3
        self.__testFile2 = "test/JiraProjectTestDataLarge.xml"
        self.__numtkts2  = 455

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

    def test_findticketype(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        tickettype = self.projectFile.findtickettype(tkt)
        self.assertNotEqual(tickettype, AG.type._unknown) #Verify that the ticket number string is not empty

    def test_findticketsummary(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        ticketsummary = self.projectFile.findticketsummary(tkt)
        self.assertTrue(ticketsummary)  #Verify that the ticket summary string is not empty

    def test_findticketstatus(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        ticketstatus = self.projectFile.findticketstatus(tkt)
        self.assertNotEqual(AG.status._unknown, ticketstatus)

    def test_findduration(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        secondsplanned = self.projectFile.findduration(tkt, AG.tags._secondsplanned)
        self.assertNotEqual(None, secondsplanned)

        secondsplanned = self.projectFile.findduration(tkt, "invalid")
        self.assertEqual (0, secondsplanned)

    def test_findcustomfield(self):
        self.projectFile.load (self.__testFile1)      
        tkt = self.projectFile.findfirstticket()
        epicfield = self.projectFile.findcustomfield(tkt, AG.tags._epiclink)
        self.assertNotEqual(None, epicfield)


    def test_findalltickets(self):        
        self.projectFile.load (self.__testFile2)       #Load a project file
        listoftickets = self.projectFile.findalltickets();
        self.assertEquals(self.__numtkts2, len(listoftickets)) 

        # The following can be uncommented for visual verification of ticket data
        #for ticket in listoftickets:
        #    print ticket, "\n"

if __name__ == '__main__':
    unittest.main()
