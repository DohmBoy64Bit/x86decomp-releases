int arithmetic(int a, int b) {
    int x = (a * 5) + (b ^ 0x13579bdf);
    return (x << 3) - (x >> 2);
}
