#!/usr/bin/python3

from statusjira import appglobal as AG

class ticket (object):
    """Class to contain the elements of a single Jira ticket"""

    def __init__(self, tktdata):
        # Note: ticketdata is provided in a tuple formatted as follows:
        # [0] str TicketNumber , [1] int TicketType   , [2] str TicketSummary, 
        # [3] int TicketStatus , [4] int SecondsPlan  , [5] int SecnodsWorked,
        # [6] int SecondsRemain, [7] str EpicReference, [8]str ScrumTeam,    
        # [9] str TicketAssignee

        self.__ticketNumber     = tktdata[0] # Text (e.g. RWS-1234)
        self.__ticketType       = tktdata[1] # Integer
        self.__ticketSummary    = tktdata[2] # Text
        self.__ticketStatus     = tktdata[3] # Integer 
        self.__ticketSecPlanned = tktdata[4] # Integer 
        self.__ticketSecWorked  = tktdata[5] # Integer 
        self.__ticketSecRemain  = tktdata[6] # Integer 
        self.__ticketEpicTicket = tktdata[7] # Text
        self.__ticketScrumTeam  = tktdata[8] # Text
        self.__ticketAssignee   = tktdata[9] # Text

    def __str__(self):
        typetext = AG.type._name.get(self.__ticketType, "Unknown")
        statustext = AG.status._text.get(self.__ticketStatus, "Unknown")
        pcttext = str(self.percentComplete())
        return str.format ("\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}%\",\"{}\"", 
                           self.number(), self.epicTicket(), self.scrumteam() , 
                           typetext     , statustext       , pcttext          , 
                           self.summary())


    def reinit (self, tktdata):
       self.__init__(tktdata)
        
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

