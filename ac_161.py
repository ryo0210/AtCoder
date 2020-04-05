# A
# a, b, c = input().split()
# print(c, a, b)

# B
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a = sorted(a, reverse=True)
# sum_a = sum(a)

# if sum_a * 1 / (4 * m) > a[m - 1]:
#     print('No')
# else:
#     print('Yes')

# C
n, k = map(int,input().split())

n = n % k
if abs(n - k) < n:
    print(abs(n - k))
else:
    print(n)

