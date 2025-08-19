/*
 * Comprehensive C11 Feature Demo for pycpp
 * This file demonstrates the newly added C11 support
 */

// C11 Keywords - These are now properly recognized and pass through

// 1. _Alignas - Alignment specifier
_Alignas(16) int aligned_array[4];
_Alignas(double) char buffer[64];

// 2. _Alignof - Alignment query in preprocessor expressions
#if _Alignof(char) == 1
    #define CHAR_ALIGN_OK 1
#endif

#if _Alignof(int) >= 4
    #define INT_ALIGN_OK 1
#endif

#if _Alignof(double) >= 8
    #define DOUBLE_ALIGN_OK 1
#endif

// 3. _Thread_local - Thread-local storage
_Thread_local int thread_counter = 0;
_Thread_local static int private_tls_var;

// 4. _Noreturn - Non-returning function attribute
_Noreturn void panic(const char* message);
_Noreturn void exit_program(int code);

// 5. _Static_assert - Compile-time assertions (passed through)
_Static_assert(sizeof(int) >= 4, "int must be at least 4 bytes");
_Static_assert(_Alignof(double) >= 8, "double alignment check");

// 6. _Generic - Generic selection expressions (in macros)
#define GENERIC_MAX(x, y) _Generic((x), \
    int: max_int, \
    float: max_float, \
    double: max_double, \
    default: max_generic \
)(x, y)

#define TYPE_SIZE(x) _Generic((x), \
    char: 1, \
    short: 2, \
    int: 4, \
    long: 8, \
    float: 4, \
    double: 8, \
    default: 0 \
)

// Usage examples
int main() {
    // Alignment-aware code
    #ifdef CHAR_ALIGN_OK
    printf("Character alignment is correct\n");
    #endif
    
    #ifdef INT_ALIGN_OK  
    printf("Integer alignment is correct\n");
    #endif
    
    // Thread-local variables
    thread_counter++;
    
    // Generic macros
    int result = GENERIC_MAX(10, 20);
    int size = TYPE_SIZE(3.14);
    
    return 0;
}

// Complex alignment checks
#if _Alignof(long long) >= 8
    #define SUPPORTS_64BIT_ALIGNMENT 1
    typedef struct {
        _Alignas(16) long long data[2];
    } aligned_struct;
#endif

// Advanced _Generic usage
#define PRINTF_DEC(x) _Generic((x), \
    char: "%c", \
    signed char: "%hhd", \
    unsigned char: "%hhu", \
    short: "%hd", \
    unsigned short: "%hu", \
    int: "%d", \
    unsigned: "%u", \
    long: "%ld", \
    unsigned long: "%lu", \
    long long: "%lld", \
    unsigned long long: "%llu", \
    float: "%f", \
    double: "%f", \
    long double: "%Lf", \
    char *: "%s", \
    void *: "%p", \
    default: "%d" \
)

#define PRINT(x) printf(PRINTF_DEC(x), x)
