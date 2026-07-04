template <class T> T clamp_value(T value, T low, T high) {
    return value < low ? low : (high < value ? high : value);
}

template <class T, unsigned N> struct Fixed {
    T values[N];
    T sum() const { T result = T(); for (unsigned i = 0; i < N; ++i) result += values[i]; return result; }
};

int templates_case(Fixed<int, 4> *values, int limit) {
    return clamp_value(values->sum(), -limit, limit);
}
