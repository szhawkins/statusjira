#!/usr/bin/python3

import sys
import getopt

class args (object):
    """Class to process command line arguments"""
        
    PROGNAME = None

    def __init__(self, argv = []):
        
        if (len(argv)):
            self.parse(argv)
        else: 
            self.parse(sys.argv)

    def parse (self, argv, verbose=False):

        type(self).PROGNAME=argv[0]
        self.__inputfile = str()  # Path to input file
        self.__outputfile = str() # Path to output file
        self.__outputfmt = str()  # Output Format (text, csv, HTML, etc)
        self.__orderby  = str()   # Orderby (Epic, Team, None, etc)
        self.__errortext= None    # If an error occurs, the text is stored here

        try: 
            optlist, args = getopt.getopt(argv[1:], ' ', ['outfile=', 
                                                          'csv',
                                                          'html',
                                                          'orderby='])
        except getopt.GetoptError as err:
            self.__errortext = err
            return False

        if (verbose):
            print ("\nargs: ", args, "     optlist: ", optlist)

        if not args:
            self.__errortext = 'The input file must be specified'
            return False
        else:
            self.__inputfile = args[0]

        for opt, val in optlist:
            if (opt == '--outfile'):
                self.__outputfile=val
            elif (opt == '--csv'):
                self.__outputfmt = 'csv' # For lower case compare
            elif (opt == '--html'):
                self.__outputfmt = 'html' # For lower case compare
            elif (opt == '--orderby'):
                self.__orderby = val.lower()    # For lower case compare

        if (verbose):
            print ("PROGNAME: ", type(self).PROGNAME)
            print ("self.__inputfile: ", self.__inputfile)
            print ("self.__outputfile: ", self.__outputfile)
            print ("self.__outputfmt: ", self.__outputfmt)
            print ("self.__orderby: ", self.__orderby)

        return True            

    def infilename(self):
        return self.__inputfile

    def outfilename(self):
        return self.__outputfile

    def outfmtcsv(self):
        return (self.__outputfmt == 'csv')

    def outfmthtml(self):
        return (self.__outputfmt == 'html')

    def orderbyepic(self):
        return (self.__orderby == 'epic')

    def orderbygroup(self):
        return (self.__orderby == 'group')

    def errortext(self):
        return (self.__errortext)

    def helptext(self):
        return "Usage: " + type(self).PROGNAME + " [OPTION]...  INPUT-FILE\n\n" + \
               "OPTIONS: \n" + \
               "--outfile=FILE\tWrite the report to FILE\n" + \
               "--csv\t\tFormat the ouptput as a .csv file\n" + \
               "--html\t\tFormat the output as an HTML file\n" 


