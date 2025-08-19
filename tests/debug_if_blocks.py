#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor
from io import StringIO

def test_if_blocks():
    """Test if #if blocks work correctly"""
    
    # Test simple expression
    p1 = Preprocessor()
    test_input1 = """#if 4 > 2
SIMPLE_WORKS
#endif"""
    
    p1.parse(test_input1)
    out1 = StringIO()
    p1.write(out1)
    result1 = out1.getvalue()
    print("Simple test result:", repr(result1))
    print("Simple test contains 'SIMPLE_WORKS':", 'SIMPLE_WORKS' in result1)
    
    # Test _Alignof expression  
    p2 = Preprocessor()
    test_input2 = """#if _Alignof(int) > 0
ALIGNOF_WORKS
#endif"""
    
    p2.parse(test_input2)
    out2 = StringIO()
    p2.write(out2)
    result2 = out2.getvalue()
    print("_Alignof test result:", repr(result2))
    print("_Alignof test contains 'ALIGNOF_WORKS':", 'ALIGNOF_WORKS' in result2)

if __name__ == '__main__':
    test_if_blocks()
