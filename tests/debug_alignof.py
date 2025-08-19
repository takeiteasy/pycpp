#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor

def test_alignof_simple():
    """Test basic _Alignof expression evaluation"""
    p = Preprocessor()
    
    # Test simple _Alignof in #if
    test_input = """#if _Alignof(int) > 0
#define TEST_PASSED 1
#endif
"""
    
    try:
        p.parse(test_input)
        print("Parsed successfully")
        print("Macros defined:", list(p.macros.keys()))
        if 'TEST_PASSED' in p.macros:
            print("✓ _Alignof evaluation works")
        else:
            print("✗ _Alignof evaluation failed - TEST_PASSED not defined")
    except Exception as e:
        print(f"✗ Parsing failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_alignof_simple()
