"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
from wyhash.backends.cffi._wyhash import ffi, lib


def hash(data: bytes, seed: int, secret: bytes) -> int:
    """
    generate hash
    :param data: bytes or bytearray to hash
    :param seed: an integer
    :param secret: 32 bytes random secret
    :return:
    """
    return lib.wyhash(
        ffi.cast("void*", ffi.from_buffer(data)),
        len(data),
        seed,
        ffi.cast("uint64_t*", ffi.from_buffer(secret)),
    )


def make_secret(seed: int) -> bytes:
    """
    make 32byte secret
    :param seed:
    :return:
    """
    _wyp = ffi.new("uint64_t[4]")
    lib.make_secret(seed, _wyp)
    return ffi.unpack(ffi.cast("char*", _wyp), 32)
