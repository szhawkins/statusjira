import unittest
from statusjira import jiraticket as JT
from statusjira import jiraproject as JP
from statusjira import projectxml as PX
from statusjira import appglobal as AG

class TestJiraTicket(unittest.TestCase):

    def setUp(self):
        self.__testFile1 = "test/JiraProjectTestData.xml"
        self.__numtkts1  = 3
        self.__testFile2 = "test/JiraProjectTestDataLarge.xml"
        self.__numtkts2  = 455

        self.__projectFile = PX.file()
        self.__projectFile.load (self.__testFile2)
        self.__listoftickets=self.__projectFile.findalltickets();

    def test_findallepics(self):

        #make sure that there are tickets in the list
        self.assertNotEqual(0, len(self.__listoftickets))

        #make sure that there are epics in the the project
        project = JP.project()
        project.findallepics(self.__listoftickets)
        self.assertNotEqual(0, len(project.listofepictickets()))

    def test_createepics(self):
        #make sure that there are tickets in the list
        self.assertNotEqual(0, len(self.__listoftickets))

        #make sure that there are epics in the the project
        project = JP.project()
        project.createepics(self.__listoftickets)
        self.assertNotEqual(0, len(project.listofepictickets()))
        self.assertNotEqual(0, len(project.listofepics()))
    
#        print project.text()
        print project.csv()         

    def test_epicinit(self):
        #make sure that there are tickets in the list
        self.assertNotEqual(0, len(self.__listoftickets))

        #make sure that there are epics in the the project
        project = JP.project()
        project.findallepics(self.__listoftickets)
        listofepictickets = project.listofepictickets()
        self.assertNotEqual(0, len(project.listofepictickets()))

if __name__ == '__main__':
    unittest.main()
