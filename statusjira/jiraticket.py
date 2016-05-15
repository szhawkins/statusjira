#!/usr/bin/python3

from statusjira import appglobal as AG

class ticket (object):
    """Class to contain the elements of a single Jira ticket"""

    def __init__(self, Number, Summary, Status, secondsplanned, 
                       secondsworked, secondsremain, EpicTicket):

        self.__ticketNumber = Number             # Text (e.g. RWS-1234)
        self.__ticketSummary = Summary           # Text
        self.__ticketStatus = Status             # Integer 
        self.__ticketSecPlanned = secondsplanned # Integer 
        self.__ticketSecWorked = secondsworked   # Integer 
        self.__ticketSecRemain = secondsremain   # Integer 
        self.__ticketEpicTicket = EpicTicket     # Text

    def number (self):
        return (self.__ticketNumber)

    def summary (self):
        return (self.__ticketSummary)

    def status (self):
        return (self.__ticketStatus)

    def secondsplanned (self):
        return (self.__ticketSecPlanned)

    def secondsworked (self):
        return (self.__ticketSecWorked)

    def secondsremain(self):
        return (self.__ticketSecRemain)

    def epicTicket(self):
        return (self.__ticketEpicTicket)

    def percentComplete(self):
        #Use the dict defined in AG.status._percentcomplete to convert
        #the ticket status in this object instance into its corresponding 
        #percent complete value

        return (AG.status._percentcomplete.get(self.__ticketStatus, AG.status._unknown))
