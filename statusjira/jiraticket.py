#!/usr/bin/python3

class ticket (object):
    """A simple class"""

    def __init__(self, Number, Summary, Status, EstHrs, 
                       WorkHrs, HrsLeft, EpicLink):

        self.__ticketNumber = Number
        self.__ticketSummary = Summary
        self.__ticketStatus = Status
        self.__ticketEstHrs = EstHrs
        self.__ticketWorkHrs = WorkHrs
        self.__ticketHrsLeft = HrsLeft
        self.__ticketEpicLink = EpicLink


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

    def epicLink(self):
        return (self.__ticketEpicLink)

