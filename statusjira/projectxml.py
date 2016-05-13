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

    def tmp (self):
        root = self.__xmlTree.getroot() #Returns the root element
        print "Root tag: ", root.tag

        for ff in root.findall("./channel/item"):
            print "ff tag: ", ff.tag



