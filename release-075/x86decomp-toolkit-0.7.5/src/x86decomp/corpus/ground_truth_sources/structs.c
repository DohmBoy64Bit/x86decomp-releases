typedef struct Pair { int x; short y; unsigned char z; } Pair;
int struct_sum(const Pair *p) { return p->x + p->y + p->z; }
