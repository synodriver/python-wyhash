# cython: language_level=3
# cython: cdivision=True
from cpython.bytes cimport PyBytes_FromStringAndSize
from libc.stdint cimport uint8_t, uint64_t

from wyhash.backends.cython cimport wyhash


cpdef inline uint64_t hash(const uint8_t[::1] data, uint64_t seed, const uint8_t[::1] secret):
    """
    generate hash
    :param data: bytes or bytearray to hash
    :param seed: an integer
    :param secret: 32 bytes random secret
    :return: 
    """
    cdef uint64_t ret
    with nogil:
        ret = wyhash.wyhash(<void*>&data[0], <size_t>data.shape[0], seed, <uint64_t*>&secret[0])
    return ret

cpdef inline bytes make_secret(uint64_t seed):
    """
    make 32byte secret
    :param seed: 
    :return: 
    """
    cdef uint64_t _wyp[4]
    with nogil:
        wyhash.make_secret(seed, _wyp)
    return PyBytes_FromStringAndSize(<char*>_wyp, 32)
