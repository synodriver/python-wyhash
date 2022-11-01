import platform
import sys

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
void make_secret(uint64_t seed, uint64_t *secret);
uint64_t wy2u0k(uint64_t r, uint64_t k);
double wy2gau(uint64_t r);
double wy2u01(uint64_t r);
uint64_t wyrand(uint64_t *seed);
uint64_t wyhash64(uint64_t A, uint64_t B);
// uint64_t _wyp[4];
uint64_t wyhash(void *key, size_t len_, uint64_t seed, const uint64_t *secret);
    """
)

source = """
#include <stdint.h>
#include "wyhash.h"
"""

ffibuilder.set_source(
    "wyhash.backends.cffi._wyhash",
    source,
    sources=[],
    include_dirs=["./dep"],
)

if __name__ == "__main__":
    ffibuilder.compile()
