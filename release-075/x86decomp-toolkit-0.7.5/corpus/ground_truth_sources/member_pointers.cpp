struct Object {
    int value;
    virtual int transform(int x) { return value + x; }
    int scale(int x) { return value * x; }
};

typedef int (Object::*member_function)(int);
int member_pointers_case(Object *object, member_function function, int value) {
    return (object->*function)(value);
}
