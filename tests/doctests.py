import unittest

class pycpp_doctests(unittest.TestCase):
    def runTest(self):
        import doctest, pycpp.preprocessor, pycpp.evaluator
        failurecount, testcount = doctest.testmod(pycpp.evaluator)
        self.assertGreater(testcount, 0)
        self.assertEqual(failurecount, 0)
        failurecount, testcount = doctest.testmod(pycpp.preprocessor)
        #self.assertGreater(testcount, 0)
        self.assertEqual(failurecount, 0)

