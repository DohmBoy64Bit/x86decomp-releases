#if defined(_MSC_VER) || defined(__clang__)
#define CDECL __cdecl
#define STDCALL __stdcall
#define FASTCALL __fastcall
#else
#define CDECL
#define STDCALL
#define FASTCALL
#endif
int CDECL cc_cdecl(int a, int b) { return a + b; }
int STDCALL cc_stdcall(int a, int b) { return a - b; }
int FASTCALL cc_fastcall(int a, int b) { return a * b; }
