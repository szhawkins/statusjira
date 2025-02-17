#!/usr/bin/python3

from statusjira import appglobal as AG
from statusjira import jiraticket as JT
from tabulate import tabulate as TABLE

class epic (object):
    """Class to contain the tickets of a single Jira epic"""

    def __init__(self, epicticket, listoftickets):
        self.__epicticket = epicticket
        self.__summary = ""
        self.__tickets = list()

        for tktdata in listoftickets:
            if (tktdata[0] == self.__epicticket):
                self.__summary = tktdata[2]        # Update the summary for this epic
            elif (tktdata[1] == AG.type._epic): 
                pass                               # Don't add an epic to another epic
            elif (tktdata[7] == epicticket):       # Add this ticket to the epic
                ticketobj = JT.ticket(tktdata)
                self.__tickets.append(ticketobj)

    def percentcomplete(self):
        epiccomplete = len(self.__tickets) * 100
        epiccurrent = 0

        for tkt in self.__tickets:
            epiccurrent += tkt.percentComplete()

        try:
            pct = ((epiccurrent*100)/epiccomplete)
        except:
            pct = 0

        return pct

    def refticket(self):
        return (self.__epicticket)

    def ticketcount(self):
        return len (self.__tickets)

    def text(self):
        result = list()

        epicstr = str.format("\nEpic: {}    Tickets: {}    Pct. Comp: {}    Summary: {}", 
                             self.__epicticket, len(self.__tickets), 
                             self.percentcomplete(), self.__summary)

        result.append(epicstr)
        
        for tkt in self.__tickets:
            result.append("\n     " + tkt.text())

        return ''.join(result)

    def csv(self):
        result = list()

        epicstr = str.format("\"Epic: {}\",\"Tickets: {}\",\" \",\" \",\"{}%\",\"Summary: {}\"\n",
                             self.__epicticket, len(self.__tickets), 
                             self.percentcomplete(), self.__summary)
                              
        result.append (epicstr)

        for tkt in self.__tickets:
            result.append("\" \"," + tkt.csv() + "\n")

        return ''.join(result)

    def txt(self):
        result = "Text formatting for project is not complete\n"
        return result

class project (object):
    
    def __init__(self):
        self.__listofepictickets = list()
        self.__listofepics = list()

    def findallepics (self, listoftickets):
        # Note: List of tickets is a list of tuples of the form:
        # str TicketNumber, int TicketType,    str TicketSummary, int TicketStatus
        # int SecondsPlan,  int SecnodsWorked, int SecondsRemain, str EpicReference
        # str ScrumTeam
    
        setofepictickets = set()

        for ticket in listoftickets:
            setofepictickets.add(ticket[7])

        self.__listofepictickets = list(setofepictickets)

    def findallteams (self, listoftickets):
        # Note: List of tickets is a list of tuples of the form:
        # str TicketNumber, int TicketType,    str TicketSummary, int TicketStatus
        # int SecondsPlan,  int SecnodsWorked, int SecondsRemain, str EpicReference
        # str ScrumTeam

        setofscrumteams = set()

        for ticket in listoftickets:
            setofscrumteams.add(ticket[8])

        self.__listofscrumteams = list(setofscrumteams)

    def createepics(self, listoftickets):

        #First, determine the number of unique epics in the list of tickets
        self.findallepics(listoftickets)

        #Second, Create one epic object for each unique epic ticket reference
        for epicticket in self.__listofepictickets:
            epicobj = epic(epicticket, listoftickets)
            self.__listofepics.append(epicobj)

    def listofepictickets(self):
        return self.__listofepictickets

    def listofscrumteams(self):
        return self.__listofscrumteams

    def listofepics(self):
        return self.__listofepics

    def ticketcount(self): 
        result = 0;

        for epic in self.__listofepics:
            result += epic.ticketcount()

        return result

    def text (self):

        result=list()
        
        projectsummary = str.format("\nProject Summary    Total Tickets: {}\n", self.ticketcount())
        result.append(projectsummary)

        for epic in self.__listofepics:
            result.append(epic.text())

        return ''.join(result)            

    def csv (self):

        result = list()

        for epic in self.__listofepics:
            result.append(epic.csv())

        return ''.join(result)

    def txt (self):

        result = list()

        for epic in self.__listofepics:
            result.append(epic.txt())

        return ''.join(result)

