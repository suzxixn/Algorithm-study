Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
n = 1260
count = 0
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count+= n // coin
    n %= coin
    print(count)

    
2
4
5
6
