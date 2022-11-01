<h1 align="center"><i>✨ python-wyhash ✨ </i></h1>

<h3 align="center">The python binding for <a href="https://github.com/wangyi-fudan/wyhash">wyhash</a> </h3>



[![pypi](https://img.shields.io/pypi/v/wyhash.svg)](https://pypi.org/project/wyhash/)
![python](https://img.shields.io/pypi/pyversions/wyhash)
![implementation](https://img.shields.io/pypi/implementation/wyhash)
![wheel](https://img.shields.io/pypi/wheel/wyhash)
![license](https://img.shields.io/github/license/synodriver/python-wyhash.svg)
![action](https://img.shields.io/github/workflow/status/synodriver/python-wyhash/build%20wheel)


### Usage

```python
import wyhash
from random import randint

seed = randint(0, 255)
sec = wyhash.make_secret(seed)
print(wyhash.hash(b"121", seed, sec))
```