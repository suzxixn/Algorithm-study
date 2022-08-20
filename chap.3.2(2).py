Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
n , m, k = map(int,input().split())
4 5 6
data = list(map(int, input().split()))
1 2 3 4
data.sort()
first = data[n-1]
second = data[n-2]
count = int(m/(k+1))*k
count += m% (k+1)
result = 0
result += (count)*first
result += (m - count)*second

print(result)
20
