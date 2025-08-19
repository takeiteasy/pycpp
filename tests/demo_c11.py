#!/usr/bin/env python3
"""
Demo script showing C11 features working in pycpp
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor
from io import StringIO

def demo_c11_features():
    """Demonstrate C11 features working"""
    p = Preprocessor()
    
    # Read the demo file
    with open('c11_demo.c', 'r') as f:
        content = f.read()
    
    print("=== C11 Demo Input ===")
    print(content[:500] + "..." if len(content) > 500 else content)
    
    # Process with pycpp
    p.parse(content)
    output_stream = StringIO()
    p.write(output_stream)
    result = output_stream.getvalue()
    
    print("\n=== C11 Demo Output ===")
    print(result)
    
    print("\n=== Macros Defined ===")
    user_macros = {k: v for k, v in p.macros.items() if not k.startswith('__')}
    for name, macro in user_macros.items():
        print(f"{name} = {macro.value}")
    
    print("\n=== C11 Features Detected ===")
    c11_features = ['_Alignas', '_Alignof', '_Thread_local', '_Noreturn', '_Static_assert', '_Generic']
    for feature in c11_features:
        if feature in result:
            print(f"✓ {feature} - properly handled")
        else:
            print(f"✗ {feature} - not found in output")

if __name__ == '__main__':
    demo_c11_features()
