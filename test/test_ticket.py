import unittest
from statusjira import jiraticket

class TestJiraTicket(unittest.TestCase):

    def setUp(self):
        self.Number = 1234
        self.Summary = "Summary"
        self.Status = 1
        self.EstHrs = 27
        self.WorkHrs = 23
        self.HrsLeft = 4
        self.EpicTicket = "RWS-9999"

    def test_createobj(self):

        ticket = jiraticket.ticket (self.Number, self.Summary, self.Status, 
                                    self.EstHrs, self.WorkHrs, self.HrsLeft, 
                                    self.EpicTicket)

        self.assertEqual (self.Number, ticket.number())
        self.assertEqual (self.Summary, ticket.summary())
        self.assertEqual (self.Status,  ticket.status())
        self.assertEqual (self.EstHrs, ticket.estimatedHrs())
        self.assertEqual (self.WorkHrs, ticket.workHrs())
        self.assertEqual (self.HrsLeft, ticket.remainingHrs())
        self.assertEqual (self.EpicTicket, ticket.epicTicket())
        
    def test_percentComplete(self):

        # The following collecton associates a ticket status value with its expected percent complete
        testdata = [(jiraticket.const._open, 0),            #  0% Complete
                    (jiraticket.const._developerTest, 50),  # 50% Complete
                    (jiraticket.const._inProgress, 25),     # 25% Complete
                    (jiraticket.const._resolved, 75),       # 75% Complete
                    (jiraticket.const._reopened, 0),        #  0% Complete
                    (jiraticket.const._closed, 100),        #100% Complete
                    (jiraticket.const._productBacklog, 0),  #  0% Complete
                    (jiraticket.const._codeReview, 50),     # 50% Complete
                    (jiraticket.const._waitingForInput, 0), #  0% Complete
                    (jiraticket.const._pendingApproval, 0)] #  0% Complete

        for record in testdata:
            ticket = jiraticket.ticket (self.Number, self.Summary, record[0], 
                                        self.EstHrs, self.WorkHrs, self.HrsLeft, 
                                        self.EpicTicket)

            self.assertEqual (record[1], ticket.percentComplete())       


if __name__ == '__main__':
    unittest.main()
