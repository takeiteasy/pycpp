#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor
from io import StringIO

def debug_char_alignment():
    """Debug the char alignment test"""
    p = Preprocessor()
    
    test_input = """TEST_START
#if _Alignof(char) == 1
CHAR_ALIGNMENT_IS_ONE
#endif
TEST_END"""
    
    p.parse(test_input)
    output_stream = StringIO()
    p.write(output_stream)
    result = output_stream.getvalue()
    
    print("Result:", repr(result))
    print("Contains CHAR_ALIGNMENT_IS_ONE:", 'CHAR_ALIGNMENT_IS_ONE' in result)
    
    # Test the expression directly
    from pycpp.evaluator import Evaluator
    e = Evaluator()
    char_align = e('_Alignof(char)')
    print(f"_Alignof(char) evaluates to: {char_align}")
    print(f"_Alignof(char) == 1 evaluates to: {e('_Alignof(char) == 1')}")

if __name__ == '__main__':
    debug_char_alignment()
