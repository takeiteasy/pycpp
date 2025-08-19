from __future__ import absolute_import, print_function
import unittest, time, difflib
try:
    clock = time.process_time
except:
    clock = time.clock

class n_std(unittest.TestCase):
    def runTest(self):
        from pycpp import Preprocessor
        import os

        start = clock()
        p = Preprocessor()
        p.compress = 1
        p.line_directive = '#'
        p.define('__STDC__ 1')
        p.define('__STDC_VERSION__ 199901L')
        p.define('__DATE__ "Jan 13 2020"')
        p.define('__TIME__ "10:47:38"')
        p.define('NO_SYSTEM_HEADERS')
        path = 'tests/test-c/n_std.c'
        with open(path, 'rt') as ih:
            p.parse(ih.read(), path)
        with open('tests/n_std.i', 'w') as oh:
            p.write(oh)
        end = clock()
        print("Preprocessed", path, "in", end-start, "seconds")
        self.assertEqual(p.return_code, 0)

        with open('tests/n_std.i', 'rt') as ih:
            written = ih.readlines()
        with open('tests/n_std-pycpp.i', 'rt') as ih:
            reference = ih.readlines()
        if written != reference:
            print("pycpp is not emitting its reference output! Differences:")
            for line in difflib.unified_diff(reference, written, fromfile='n_std-pycpp.i', tofile='n_std.i'):
                print(line, end='')
            self.assertTrue(False)
        
