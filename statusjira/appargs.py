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
    
    def __str__(self):

        if (self.__errortext):
            errtxt = self.__errortext
        else:
            errtxt = str()

        return "self.__inputfile:    " + self.__inputfile  + \
               "\nself.__outputfile: " + self.__outputfile + \
               "\nself.__outputfmt:  " + self.__outputfmt  + \
               "\nself.__orderby:    " + self.__orderby    + \
               "\nself.__errortext:  " + errtxt

    def parse (self, argv, verbose=False):

        type(self).PROGNAME=argv[0]
        self.__inputfile = str()        # Path to input file
        self.__outputfile = str()       # Path to output file
        self.__outputfmt = str()        # Output Format (text, csv, HTML, etc)
        self.__groupby  = str()         # Group By: (Epic, Team, None, etc)
        self.__include_subtasks = False # Flag to enable subtasks in reports
        self.__errortext= None          # If an error occurs, the text is stored here

        try: 
            optlist, args = getopt.getopt(argv[1:], '-h', ['outfile=', 
                                                           'csv',
                                                           'html',
                                                           'groupepics',
                                                           'groupteams',
                                                           'include-subtasks',
                                                           'help'])
        except getopt.GetoptError as err:
            self.__errortext = err.__str__()
            return False

        if (verbose):
            print ("\nargs: ", args, "     optlist: ", optlist)

        for opt, val in optlist:
            if (opt == '--outfile'):
                self.__outputfile=val
            elif (opt == '--csv'):
                self.__outputfmt = 'csv'  # For lower case compare
            elif (opt == '--html'):
                self.__outputfmt = 'html' # For lower case compare
            elif (opt == '--groupepics'):
                self.__groupby = 'epic'   # For lower case compare
            elif (opt == '--groupteams'):
                self.__groupby = 'team'
            elif (opt == '--include-subtasks'):
                self.__include_subtasks = True
            elif opt in ("-h", "--help"):
                print ()
                print (self.helptext())
                sys.exit()

        if not args:
            self.__errortext = 'The input file must be specified'
            return False
        else:
            self.__inputfile = args[0]

        if (verbose):
            print ("PROGNAME: ", type(self).PROGNAME)
            print ("self.__inputfile: ", self.__inputfile)
            print ("self.__outputfile: ", self.__outputfile)
            print ("self.__outputfmt: ", self.__outputfmt)
            print ("self.__groupby: ", self.__groupby)
            print ("self.__include-subtasks: ", self.__include_subtasks)

        return True            

    def infilename(self):
        return self.__inputfile

    def outfilename(self):
        return self.__outputfile

    def outfmtcsv(self):
        return (self.__outputfmt == 'csv')

    def outfmthtml(self):
        return (self.__outputfmt == 'html')

    def groupepics(self):
        return (self.__groupby == 'epic')

    def groupteams(self):
        return (self.__groupby == 'team')

    def errortext(self):
        return (self.__errortext)

    def include_subtasks(self):
        return (self.__include_subtasks)

    def helptext(self):
        return "Usage: " + type(self).PROGNAME + " [OPTION]...  INPUT-FILE\n\n"     + \
               "OPTIONS: \n" + \
               "--outfile=FILE\tWrite the report to FILE\n"                         + \
               "--csv\t\tFormat the ouptput as a .csv file\n"                       + \
               "--html\t\tFormat the output as an HTML file\n"                      + \
               "--include-subtasks  Include Subtask tickets in the output report\n" + \
               "--help, -h\tHelp\n"

