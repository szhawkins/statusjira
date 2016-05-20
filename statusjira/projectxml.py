#!/usr/bin/python3
import xml.etree.ElementTree as ET
import statusjira.appglobal as AG

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

    def findtickettype(self, ticketelement):
        try:
            type_element = ticketelement.find("type")
            type_text = type_element.get ("id")
            type_int = int (type_text)
        except:             
            type_int = AG.type._unknown
        return type_int

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
            status_int = AG.status._unknown

        if (not status_int in AG.status._valid):
            status_int = AG.status._unknown

        return status_int

    def findduration(self, ticketelement, durationattribute):
        duration_element = ticketelement.find(durationattribute)
        duration_int = 0

        if (not None == duration_element):
            duration_text = duration_element.get("seconds")

            try: 
                duration_int = int (duration_text)
            except:
                duration_int = 0

        return duration_int            

    def findcustomfield(self, ticketelement, fieldname):

        epiclink = "None"

        for fieldelement in ticketelement.findall(".//" + AG.tags._customfield):
            nameelement = fieldelement.find (AG.tags._customfieldname)
            valueelement = fieldelement.find (AG.tags._customfieldvalue)

            if (nameelement != None)  and (valueelement != None):
                if (nameelement.text == fieldname):
                    epiclink = valueelement.text

        return epiclink

    def findepicref(self, ticketelement):
        tktepic = self.findcustomfield(ticketelement, AG.tags._epiclink)
        tkttype = self.findtickettype(ticketelement)

        if (tkttype == AG.type._sccbreq):
            result = "SCCB Request"
        else:
            result = tktepic

        return result            
       


    def findalltickets (self):
        alltickets = list()             #alltickets is returned by this operation
        root = self.__xmlTree.getroot() #Returns the root element

        for tktelement in root.findall("./channel/item"):

            tktNumber = self.findticketnumber(tktelement)                          # Text (e.g. RWS-1234)
            tktType = self.findtickettype(tktelement)                              # Integer (Type ID)
            tktSummary = self.findticketsummary(tktelement)                        # Text
            tktStatus = self.findticketstatus(tktelement)                          # Integer
            tktsecplanned = self.findduration(tktelement, AG.tags._secondsplanned) # Integer
            tktsecworked = self.findduration(tktelement, AG.tags._secondsworked)   # Integer
            tktsecremain = self.findduration(tktelement, AG.tags._secondsremain)   # Integer
            tktEpicRef = self.findepicref(tktelement)                              # Text (e.g. RWS-7890)

            alltickets.append ((tktNumber, tktType, tktSummary, tktStatus,
                               tktsecplanned, tktsecworked, tktsecremain,
                               tktEpicRef))

        return alltickets


