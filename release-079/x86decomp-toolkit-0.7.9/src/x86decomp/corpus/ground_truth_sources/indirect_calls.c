typedef int (*operation_fn)(int, int);

int indirect_calls_case(operation_fn operation, int left, int right) {
    if (!operation) return -1;
    return operation(left, right) + operation(right, left);
}
