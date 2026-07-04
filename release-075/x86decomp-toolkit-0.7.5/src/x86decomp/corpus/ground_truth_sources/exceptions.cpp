extern "C" int exception_path(int x) {
    try {
        if (x < 0) throw x;
        return x + 5;
    } catch (int value) {
        return -value;
    }
}
