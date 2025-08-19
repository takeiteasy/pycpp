#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor

def test_if_expression_debug():
    """Debug what happens in #if expressions"""
    p = Preprocessor()
    
    # Test simple expression
    test_input1 = """#if 4 > 2
#define SIMPLE_TEST 1
#endif
"""
    
    # Test _Alignof expression  
    test_input2 = """#if _Alignof(int) > 0
#define ALIGNOF_TEST 1
#endif
"""
    
    print("Testing simple expression...")
    p.parse(test_input1)
    print("Macros after simple test:", [k for k in p.macros.keys() if not k.startswith('__')])
    
    print("\nTesting _Alignof expression...")
    p2 = Preprocessor()
    p2.parse(test_input2)
    print("Macros after _Alignof test:", [k for k in p2.macros.keys() if not k.startswith('__')])
    
    # Let's also check the tokens that get generated for the expression
    tokens = p2.tokenize('_Alignof(int) > 0')
    print("Tokens for '_Alignof(int) > 0':", [(t.type, t.value) for t in tokens])

if __name__ == '__main__':
    test_if_expression_debug()
