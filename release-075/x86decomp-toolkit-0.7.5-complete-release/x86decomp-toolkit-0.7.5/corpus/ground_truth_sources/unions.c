union Number { unsigned bits; float value; };

unsigned unions_case(float input) {
    union Number number;
    number.value = input;
    number.bits ^= 0x80000000u;
    return number.bits;
}
