"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
import os
import platform

impl = platform.python_implementation()


def _should_use_cffi() -> bool:
    ev = os.getenv("WYHASH_USE_CFFI")
    if ev is not None:
        return True
    if impl == "CPython":
        return False
    else:
        return True


if not _should_use_cffi():
    from wyhash.backends.cython import hash, make_secret
else:
    from wyhash.backends.cffi import hash, make_secret
