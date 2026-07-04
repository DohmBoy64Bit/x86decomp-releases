int aliasing(int *a, int *b) {
    int before = *a;
    *b += 3;
    *a ^= *b;
    return before + *a;
}
