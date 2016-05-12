#!/usr/bin/python3

class ticket (object):
    """A simple class"""

    def __init__(self, Number, Description, Status, EstHrs, 
                       WorkHrs, HrsLeft, EpicLink):

        self.__ticketNumber = 0
        self.__ticketDescription = ""
        self.__ticketStatus = 0
        self.__ticketEstHrs = 0
        self.__ticketWorkHrs = 0
        self.__ticketHrsLeft = 0
        self.__ticketEpicLink = ""



