int loops_case(const int *values, unsigned count) {
    int sum = 0;
    unsigned index = 0;
    while (index < count) {
        if (values[index] > 0) sum += values[index];
        else sum -= index;
        ++index;
    }
    return sum;
}
