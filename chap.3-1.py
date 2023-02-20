Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 1260
>>> count = 0
>>> 
>>> coin_types = [500, 100, 50, 10]
>>> 
>>> for coin in coin_types:
...     count += n // coin
...     n %= coin
... 
...     
>>> print(count)
6
