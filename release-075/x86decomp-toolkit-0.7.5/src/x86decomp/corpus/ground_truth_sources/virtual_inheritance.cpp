struct Root { int value; virtual int get() const { return value; } };
struct Left : virtual Root { int left; int get() const override { return value + left; } };
struct Right : virtual Root { int right; int get() const override { return value + right; } };
struct Diamond : Left, Right { int extra; int get() const override { return value + left + right + extra; } };

int virtual_inheritance_case(Diamond *object) { return object->get(); }
