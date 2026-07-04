struct Left { virtual int left() { return 1; } };
struct Right { virtual int right() { return 2; } };
struct Both : Left, Right { int left() override { return 3; } int right() override { return 4; } };
extern "C" int multi_call(Both *p) { return p->left() + p->right(); }
