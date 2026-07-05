#include <stdarg.h>

int varargs_case(unsigned count, ...) {
    va_list args;
    int total = 0;
    va_start(args, count);
    for (unsigned index = 0; index < count; ++index) total += va_arg(args, int);
    va_end(args);
    return total;
}
