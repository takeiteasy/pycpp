#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp.evaluator import Evaluator

def test_alignof_evaluator():
    """Test _Alignof in the expression evaluator directly"""
    e = Evaluator()
    
    try:
        # Test simple expression
        result = e('4 > 2')
        print(f"Simple expr (4 > 2): {result}")
        
        # Test _Alignof expression
        result = e('_Alignof(int)')
        print(f"_Alignof(int): {result}")
        
        # Test _Alignof in comparison
        result = e('_Alignof(int) > 0')
        print(f"_Alignof(int) > 0: {result}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_alignof_evaluator()
