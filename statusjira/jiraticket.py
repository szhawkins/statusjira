#!/usr/bin/python3

class ticket (object):
    """A simple class"""

    def __init__(self, Number, Summary, Status, EstHrs, 
                       WorkHrs, HrsLeft, EpicLink):

        self.__ticketNumber = Number
        self.__ticketSummary = Summary
        self.__ticketStatus = 0
        self.__ticketEstHrs = 0
        self.__ticketWorkHrs = 0
        self.__ticketHrsLeft = 0
        self.__ticketEpicLink = ""


    def number (self):
        return (self.__ticketNumber)

    def summary (self):
        return (self.__ticketSummary)

