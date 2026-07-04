struct Counter { int value; Counter() : value(41) {} };
Counter global_counter;
extern "C" int static_value() { return global_counter.value; }
