double floating_point_case(double a, double b, int mode) {
    double value = a * 1.5 + b / 3.0;
    if (mode & 1) value = value * value;
    if (mode & 2) value = value - a;
    return value;
}
