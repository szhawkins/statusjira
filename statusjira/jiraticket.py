#!/usr/bin/python3

from statusjira import appglobal as AG

class ticket (object):
    """Class to contain the elements of a single Jira ticket"""

    def __init__(self, Number, Type, Summary, Status, secondsplanned, 
                       secondsworked, secondsremain, EpicTicket, scrumteam):

        self.__ticketNumber = Number             # Text (e.g. RWS-1234)
        self.__ticketType = Type                 # Integer
        self.__ticketSummary = Summary           # Text
        self.__ticketStatus = Status             # Integer 
        self.__ticketSecPlanned = secondsplanned # Integer 
        self.__ticketSecWorked = secondsworked   # Integer 
        self.__ticketSecRemain = secondsremain   # Integer 
        self.__ticketEpicTicket = EpicTicket     # Text
        self.__ticketScrumTeam = scrumteam       # Text

    def __str__(self):
        typetext = AG.type._name.get(self.__ticketType, "Unknown")
        statustext = AG.status._text.get(self.__ticketStatus, "Unknown")
        pcttext = str(self.percentComplete())
        return str.format ("\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}%\",\"{}\"", 
                           self.number(), self.epicTicket(), self.scrumteam() , 
                           typetext     , statustext       , pcttext          , 
                           self.summary())


    def reinit (self, tktdata):
        # Note: ticketdata is provided in a tuple formatted as follows:
        # str TicketNumber, int TicketType,    str TicketSummary, int TicketStatus
        # int SecondsPlan,  int SecnodsWorked, int SecondsRemain, str EpicReference
        # str ScrumTeam
       self.__init__(tktdata[0], tktdata[1], tktdata[2], tktdata[3], tktdata[4],
                     tktdata[5], tktdata[6], tktdata[7], tktdata[8])
        
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

    def scrumteam(self):
        return (self.__ticketScrumTeam)

    def type (self): 
        return (self.__ticketType)

    def percentComplete(self):
        #Use the dict defined in AG.status._percentcomplete to convert
        #the ticket status in this object instance into its corresponding 
        #percent complete value

        return (AG.status._percentcomplete.get(self.__ticketStatus, AG.status._unknown))

    def text(self):
        typetext = AG.type._name.get(self.__ticketType, "Unknown")
        statustext = AG.status._text.get(self.__ticketStatus, "Unknown")
        pcttext = str(self.percentComplete())

        return str.format ("Ticket: {}  Type: {}  Status: {}  Pct comp: {}  Summary: {}", 
                           self.number(), typetext, statustext, pcttext, self.summary())


    def csv(self):
        typetext = AG.type._name.get(self.__ticketType, "Unknown")
        statustext = AG.status._text.get(self.__ticketStatus, "Unknown")
        pcttext = str(self.percentComplete())

        return str.format ("\"{}\",\"{}\",\"{}\",\"{}%\",\"{}\"", 
                           self.number(), typetext, statustext, pcttext, self.summary())

