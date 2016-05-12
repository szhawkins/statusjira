import unittest
from statusjira import jiraticket

class TestJiraTicket(unittest.TestCase):

    def test_createobj(self):
        Number = 1234
        Description = "This is a test ticket"
        Status = 1
        EstHrs = 27
        WorkHrs = 23
        HrsLeft = 4
        EpicLink = "foo.com"

        ticket = jiraticket.ticket (Number, Description, Status, 
                                    EstHrs, WorkHrs,     HrsLeft, 
                                    EpicLink)

        **** Test methods: number, description, status, esthrs, workhrs, remainhrs, epiclink ***


if __name__ == '__main__':
    unittest.main()
