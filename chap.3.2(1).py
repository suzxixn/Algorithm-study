Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
n, m, k = map(int, input().split())
5 8 3
data = list(map(int, input().split()))
2 4 5 4 6
data.sort()
first = data[n-1]
second = data[n-2]
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
        if m == 0:
            break
        result += second
        m -= 1

        
print(result)