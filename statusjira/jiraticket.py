#!/usr/bin/python3

class const (object):
    """Constants used by the jiraticket module"""

    _unknown = -1            #Status value is not available
    _open = 1                #Verified in Jira
    _developerTest = 10006   #Verified in Jira   
    _inProgress = 3          #Verified in Jira
    _resolved = 5            #Verified in Jira
    _reopened = 992          # -- Not Verified --
    _closed = 6              #Verified in Jira
    _productBacklog = 991    # -- Not Verified --
    _codeReview = 10004      #Verified in Jira
    _waitingForInput = 10822 #Verified in Jira
    _pendingApproval = 10021 #Verified in Jira

    _pctOpen = 0
    _pctDeveloperTest = 50
    _pctInProgress = 25
    _pctResolved = 75
    _pctReopened = 0
    _pctClosed = 100
    _pctProductBacklog = 0
    _pctCodeReview = 50
    _pctWaitingForInput = 0
    _pctPendingApproval = 0

class ticket (object):
    """Class to contain the elements of a single Jira ticket"""

    def __init__(self, Number, Summary, Status, EstHrs, 
                       WorkHrs, HrsLeft, EpicTicket):

        self.__ticketNumber = Number         # Text (e.g. RWS-1234)
        self.__ticketSummary = Summary       # Text
        self.__ticketStatus = Status         # Integer -->Change to sec_planned
        self.__ticketEstHrs = EstHrs         # Integer -->Change to sec_worked
        self.__ticketWorkHrs = WorkHrs       # Integer -->Change to sec_remain
        self.__ticketHrsLeft = HrsLeft       # Integer
        self.__ticketEpicTicket = EpicTicket # Text


    def number (self):
        return (self.__ticketNumber)

    def summary (self):
        return (self.__ticketSummary)

    def status (self):
        return (self.__ticketStatus)

    def estimatedHrs (self):
        return (self.__ticketEstHrs)

    def workHrs (self):
        return (self.__ticketWorkHrs)

    def remainingHrs(self):
        return (self.__ticketHrsLeft)

    def epicTicket(self):
        return (self.__ticketEpicTicket)

    def percentComplete(self):
        if self.__ticketStatus == const._open:
            return (const._pctOpen)
        elif self.__ticketStatus == const._developerTest:
            return (const._pctDeveloperTest)
        elif self.__ticketStatus == const._inProgress:
            return (const._pctInProgress)
        elif self.__ticketStatus == const._resolved:
            return (const._pctResolved)
        elif self.__ticketStatus == const._closed:
            return (const._pctClosed)
        elif self.__ticketStatus == const._productBacklog:
            return (const._pctProductBacklog)
        elif self.__ticketStatus == const._codeReview:
            return (const._pctCodeReview)
        else:
            return (0)



