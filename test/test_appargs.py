import unittest
from statusjira import appargs as ARGS

class TestArgs(unittest.TestCase):

    def setUp(self):
        self._argv = ['ExecutableName']
        self._args = ARGS.args()
        self._infilename = "InputFile.dat"
        self._outfilename = "OutputFile.dat"
        self._beverbose = False

    def test_arg_infile(self):
        self._argv.append(self._infilename)
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertEqual (self._infilename, self._args.infilename())
        
    def test_opt_outfile(self):
        self._argv.append ('--outfile='+self._outfilename)
        self._argv.append (self._infilename)
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertEqual (self._outfilename, self._args.outfilename())

    def test_opt_outfmt(self):
        self._argv.append ('--csv')
        self._argv.append (self._infilename)
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertIsNone(self._args.errortext())
        self.assertTrue (self._args.outfmtcsv())
        self.assertFalse(self._args.outfmthtml())

        self._argv[1] = '--html'
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertFalse(self._args.outfmtcsv())
        self.assertTrue (self._args.outfmthtml())

    def test_no_args(self):
        # Parsing the commandline with no arguments
        self.assertFalse(self._args.parse(self._argv, self._beverbose))
        self.assertIsNotNone(self._args.errortext())

    def test_invalid_args(self):
        self._argv.append ('--invalidarg')
        self.assertFalse(self._args.parse(self._argv, self._beverbose))
        self.assertIsNotNone(self._args.errortext())

    def test_noargvalue(self):
        self._argv.append('--outfile')
        self.assertFalse(self._args.parse(self._argv, self._beverbose))
        self.assertIsNotNone(self._args.errortext())

    def test_opt_orderby(self):
        self._argv.append('--orderby=epic')
        self._argv.append('self._infilename')
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertIsNone(self._args.errortext())
        self.assertTrue (self._args.orderbyepic())

        self._argv[1] = '--orderby=group'
        self.assertTrue(self._args.parse(self._argv, self._beverbose))
        self.assertIsNone(self._args.errortext())
        self.assertTrue (self._args.orderbygroup())

    def test_helptext(self):
        self._argv.append(self._infilename)
        self.assertTrue(self._args.parse(self._argv, self._beverbose))

        if (self._beverbose):
            print self._args.helptext()
        
        
