extern int tail_target(int value);

int tail_calls_case(int value) {
    if (value < 0) return -value;
    return tail_target(value + 1);
}
