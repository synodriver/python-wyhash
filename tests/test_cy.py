"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
from random import randint
from unittest import TestCase

from wyhash import hash, make_secret


class TestAll(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hash(self):
        # bytes([randint(0, 255) for _ in range(1000)])
        for i in range(1000):
            sec = make_secret(randint(0, 255))
            self.assertEqual(hash(b"asasa", 0, sec), hash(b"asasa", 0, sec))
            self.assertNotEqual(hash(b"asasa", 0, sec), hash(b"asasa", 1, sec))