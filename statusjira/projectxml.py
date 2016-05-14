#!/usr/bin/python3
import xml.etree.ElementTree as ET

class const (object):
    """Constants used by the jiraticket module"""

    _tmp = 1

class file (object):
    """Class to read and parse Jira offload in XML format"""

    def __init__(self):
        self.__fileName = ""

    def load (self, fileName):
        self.__fileName = "" #Filename property remains empty until file is successfully loaded

        try:
            self.__xmlTree = ET.parse(fileName)
            self.__fileName = fileName
        except IOError:
            self.__fileName = "" #If file is not loaded, filename property remains empty

    def fileName(self):
        return self.__fileName

    def findfirstticket(self):
        root = self.__xmlTree.getroot()     #Returns the root element of the XML document
        return root.find("./channel/item")  #Returns the root element of the first ticket
    
    def findticketnumber(self, ticketelement):
        number_element = ticketelement.find("key")
        number_text = number_element.text       
        return number_text

    def findticketsummary(self, ticketelement):
        summary_element = ticketelement.find("summary")
        summary_text = summary_element.text       
        return summary_text

    def findticketstatus(self, ticketelement):
        status_element = ticketelement.find("status")
        status_text = status_element.get("id")
        try: 
            status_int = int (status_text)
        except:
            status_int = -1

        valid_status = [1, 10006, 3, 5, 992, 6, 991, 10004, 10822, 10021]

        if (not status_int in valid_status):
            status_int = -1

        return status_int

    def findalltickets (self):
        alltickets = list()             #alltickets is returned by this operation
        root = self.__xmlTree.getroot() #Returns the root element

        for tktelement in root.findall("./channel/item"):

            tktNumber = self.findticketnumber(tktelement)    # Text (e.g. RWS-1234)
            tktSummary = self.findticketsummary(tktelement)  # Text
            tktStatus = self.findticketstatus(tktelement)    # Integer
            tktEstHrs =  0             # Integer
            tktWorkHrs = 0             # Integer
            tktHrsLeft = 0             # Integer
            tktEpicRef = "tktEpicRef"  # Text (e.g. RWS-7890)

            alltickets.append ((tktNumber, tktSummary, tktStatus,
                               tktEstHrs, tktWorkHrs, tktHrsLeft,
                               tktEpicRef))

        return alltickets


