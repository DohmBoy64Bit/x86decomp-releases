#if defined(_MSC_VER)
__declspec(thread) int corpus_tls = 23;
#elif defined(__clang__)
__declspec(thread) int corpus_tls = 23;
#else
_Thread_local int corpus_tls = 23;
#endif
int tls_increment(int x) { corpus_tls += x; return corpus_tls; }
