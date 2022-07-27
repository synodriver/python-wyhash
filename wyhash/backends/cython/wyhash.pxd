# cython: language_level=3
# cython: cdivision=True
from libc.stdint cimport uint64_t


cdef extern from "wyhash.h" nogil:
    void make_secret(uint64_t seed, uint64_t *secret)
    uint64_t wy2u0k(uint64_t r, uint64_t k)
    double wy2gau(uint64_t r)
    double wy2u01(uint64_t r)
    uint64_t wyrand(uint64_t *seed)
    uint64_t wyhash64(uint64_t A, uint64_t B)
    uint64_t _wyp[4]
    uint64_t wyhash(void *key, size_t len_, uint64_t seed, const uint64_t *secret)