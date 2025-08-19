#!/usr/bin/env python3
"""
Test file for C11 features in pycpp
"""

import os
import sys
import tempfile
from io import StringIO

# Add the pycpp module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pycpp import Preprocessor

def test_c11_keywords():
    """Test that C11 keywords are properly tokenized"""
    p = Preprocessor()
    
    # Test _Generic
    tokens = p.tokenize('_Generic')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_GENERIC'
    assert tokens[0].value == '_Generic'
    
    # Test _Static_assert
    tokens = p.tokenize('_Static_assert')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_STATIC_ASSERT'
    assert tokens[0].value == '_Static_assert'
    
    # Test _Alignof
    tokens = p.tokenize('_Alignof')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_ALIGNOF'
    assert tokens[0].value == '_Alignof'
    
    # Test _Alignas
    tokens = p.tokenize('_Alignas')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_ALIGNAS'
    assert tokens[0].value == '_Alignas'
    
    # Test _Thread_local
    tokens = p.tokenize('_Thread_local')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_THREAD_LOCAL'
    assert tokens[0].value == '_Thread_local'
    
    # Test _Noreturn
    tokens = p.tokenize('_Noreturn')
    assert len(tokens) == 1
    assert tokens[0].type == 'CPP_NORETURN'
    assert tokens[0].value == '_Noreturn'
    
    print("✓ All C11 keyword tokenization tests passed")

def test_c11_in_preprocessor():
    """Test C11 features in preprocessor context"""
    p = Preprocessor()
    
    # Test that C11 keywords pass through
    test_input = """
#define ALIGN16 _Alignas(16)
#define NORET _Noreturn

ALIGN16 int x;
NORET void fatal(void);

_Thread_local int tls_var;
_Static_assert(sizeof(int) >= 4, "int too small");
"""
    
    p.parse(test_input)
    output_stream = StringIO()
    p.write(output_stream)
    result = output_stream.getvalue()
    
    # Check that C11 keywords appear in output
    assert '_Alignas(16)' in result
    assert '_Noreturn' in result
    assert '_Thread_local' in result
    assert '_Static_assert' in result
    
    print("✓ C11 keywords pass through preprocessor correctly")

def test_alignof_in_expressions():
    """Test _Alignof in preprocessor expressions"""
    p = Preprocessor()
    
    # Test _Alignof in #if expressions
    test_input = """
#if _Alignof(int) > 2
#define HAS_LARGE_INT_ALIGNMENT 1
#else
#define HAS_LARGE_INT_ALIGNMENT 0
#endif

#if _Alignof(double) >= 8
#define HAS_8_BYTE_DOUBLE_ALIGNMENT 1
#endif

TEST_CONTENT_START
#if _Alignof(char) == 1
CHAR_ALIGNMENT_IS_ONE
#endif
TEST_CONTENT_END
"""
    
    p.parse(test_input)
    output_stream = StringIO()
    p.write(output_stream)
    result = output_stream.getvalue()
    
    # Check that _Alignof expressions work in #if directives
    assert 'CHAR_ALIGNMENT_IS_ONE' in result
    assert 'TEST_CONTENT_START' in result
    assert 'TEST_CONTENT_END' in result
    
    # Check that macros were defined based on _Alignof evaluations
    assert 'HAS_LARGE_INT_ALIGNMENT' in p.macros
    assert p.macros['HAS_LARGE_INT_ALIGNMENT'].value[0].value == '1'
    
    assert 'HAS_8_BYTE_DOUBLE_ALIGNMENT' in p.macros
    assert p.macros['HAS_8_BYTE_DOUBLE_ALIGNMENT'].value[0].value == '1'
    
    print("✓ _Alignof in expressions works correctly")

def test_generic_in_macros():
    """Test _Generic in macro definitions"""
    p = Preprocessor()
    
    test_input = """
#define GENERIC_ABS(x) _Generic((x), \\
    int: abs, \\
    float: fabsf, \\
    double: fabs, \\
    default: abs \\
)(x)

#define TYPE_SIZE(x) _Generic((x), \\
    char: 1, \\
    int: 4, \\
    double: 8, \\
    default: sizeof(x) \\
)

int result = GENERIC_ABS(-5);
int size = TYPE_SIZE(3.14);
"""
    
    p.parse(test_input)
    output_stream = StringIO()
    p.write(output_stream)
    result = output_stream.getvalue()
    
    # Check that _Generic expressions are preserved and expanded
    assert '_Generic' in result
    assert 'abs' in result or 'fabs' in result
    
    print("✓ _Generic in macros works correctly")

def run_all_tests():
    """Run all C11 tests"""
    print("Testing C11 support in pycpp...")
    
    try:
        test_c11_keywords()
        test_c11_in_preprocessor() 
        test_alignof_in_expressions()
        test_generic_in_macros()
        
        print("\n🎉 All C11 tests passed! The upgrade was successful.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    run_all_tests()
