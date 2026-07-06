struct Base {
    virtual int value(int x) { return x + 1; }
    virtual ~Base() {}
};
struct Derived : Base {
    int bias;
    Derived() : bias(7) {}
    int value(int x) override { return x + bias; }
};
extern "C" int virtual_call(Base *p, int x) { return p->value(x); }
