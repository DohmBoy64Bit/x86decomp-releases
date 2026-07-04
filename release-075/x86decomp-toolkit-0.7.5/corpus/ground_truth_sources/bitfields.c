struct Flags {
    unsigned enabled : 1;
    unsigned mode : 3;
    signed delta : 7;
    unsigned count : 12;
};

int bitfield_case(struct Flags *flags, unsigned value) {
    flags->mode = value & 7u;
    flags->count += value;
    return flags->enabled ? flags->delta + (int)flags->count : -(int)flags->mode;
}
