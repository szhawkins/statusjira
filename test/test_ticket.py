import unittest
from statusjira import jiraticket as jt
from statusjira import appglobal as AG

class TestJiraTicket(unittest.TestCase):

    def setUp(self):
        self.Number = 1234
        self.Type = AG.type._story
        self.Summary = "Summary"
        self.Status = AG.status._open
        self.secondsplanned = 1000
        self.secondsworked = 500
        self.secondsremain = 3456
        self.EpicTicket = "RWS-9999"
        self.scrumteam = "Unit Test"

    def test_createobj(self):

        ticket = jt.ticket (self.Number, self.Type, self.Summary, self.Status, 
                                    self.secondsplanned, self.secondsworked, 
                                    self.secondsremain, self.EpicTicket, self.scrumteam)

        self.assertEqual (self.Number, ticket.number())
        self.assertEqual (self.Type, ticket.type())
        self.assertEqual (self.Summary, ticket.summary())
        self.assertEqual (self.Status,  ticket.status())
        self.assertEqual (self.secondsplanned, ticket.secondsplanned())
        self.assertEqual (self.secondsworked, ticket.secondsworked())
        self.assertEqual (self.secondsremain, ticket.secondsremain())
        self.assertEqual (self.EpicTicket, ticket.epicTicket())
        
    def test_percentComplete(self):

        # The following collecton associates a ticket status value with its expected percent complete
        testdata = [(AG.status._open, 0),            #  0% Complete
                    (AG.status._developerTest, 50),  # 50% Complete
                    (AG.status._inProgress, 25),     # 25% Complete
                    (AG.status._resolved, 75),       # 75% Complete
                    (AG.status._reopened, 0),        #  0% Complete
                    (AG.status._closed, 100),        #100% Complete
                    (AG.status._productBacklog, 0),  #  0% Complete
                    (AG.status._codeReview, 50),     # 50% Complete
                    (AG.status._waitingForInput, 0), #  0% Complete
                    (AG.status._pendingApproval, 0)] #  0% Complete

        for record in testdata:
            ticket = jt.ticket (self.Number, self.Type, self.Summary, record[0], 
                                        self.secondsplanned, self.secondsworked, 
                                        self.secondsremain, self.EpicTicket,
                                        self.scrumteam)

            self.assertEqual (record[1], ticket.percentComplete())       


if __name__ == '__main__':
    unittest.main()
