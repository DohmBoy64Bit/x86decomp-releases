struct ErrorA { int value; };
struct ErrorB { int value; };
extern int may_throw(int);

int eh_multiple_case(int input) {
    try {
        int result = may_throw(input);
        if (result == 1) throw ErrorA{input};
        if (result == 2) throw ErrorB{input};
        return result;
    } catch (const ErrorA &error) {
        return error.value + 10;
    } catch (const ErrorB &error) {
        return error.value + 20;
    } catch (...) {
        return -1;
    }
}
