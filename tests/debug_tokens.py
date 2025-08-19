#!/usr/bin/env python3
"""
Debug C11 tokenization
"""

import os
import sys

# Add the pycpp module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor

def debug_tokenization():
    """Debug what tokens are being generated"""
    p = Preprocessor()
    
    # Test _Generic
    tokens = p.tokenize('_Generic')
    print(f"_Generic tokens: {[(t.type, t.value) for t in tokens]}")
    
    # Test regular identifier
    tokens = p.tokenize('identifier')
    print(f"identifier tokens: {[(t.type, t.value) for t in tokens]}")
    
    # Test _Static_assert
    tokens = p.tokenize('_Static_assert')
    print(f"_Static_assert tokens: {[(t.type, t.value) for t in tokens]}")

if __name__ == '__main__':
    debug_tokenization()
