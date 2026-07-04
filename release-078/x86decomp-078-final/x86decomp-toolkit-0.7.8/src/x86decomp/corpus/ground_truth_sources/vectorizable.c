void vectorizable_case(float *restrict output, const float *restrict left,
                       const float *restrict right, unsigned count) {
    for (unsigned index = 0; index < count; ++index)
        output[index] = left[index] * 2.0f + right[index];
}
