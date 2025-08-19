from __future__ import absolute_import, print_function
import unittest, sys

shouldbe = r'''#line 1 "tests/issue0037/inc.h"
    /** this spans
        two lines */
    virtual std::string baseOnly();
'''

class runner(object):
    def runTest(self):
        from pycpp import CmdPreprocessor
        p = CmdPreprocessor(['pycpp', '--time', '--passthru-comments',
                             '-o', 'tests/issue0037.i',
                             'tests/issue0037/inc.h'])
        with open('tests/issue0037.i', 'rt') as ih:
            output = ih.read()
        if output != shouldbe:
            print("Should be:\n" + shouldbe + "EOF\n", file = sys.stderr)
            print("\nWas:\n" + output + "EOF\n", file = sys.stderr)
        self.assertEqual(p.return_code, 0)
        self.assertEqual(output, shouldbe)

class multiline_comments(unittest.TestCase, runner):
    pass
