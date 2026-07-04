int branches(int x, int y) {
    if (x < 0) return y - x;
    if (x == y) return x * 3;
    return x > y ? x + 7 : y + 11;
}
