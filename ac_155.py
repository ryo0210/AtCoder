# A AC
# a, b, c = map(int, input().split())
# if a == b ==c:
#     print('No')
# elif a == b or b == c or a ==c:
#     print('Yes')
# else:
#     print('No')

# B AC
# n = int(input())
# a = list(map(int, input().split()))
# flag = 0

# for i in a:
#     if i % 2 == 0:
#         if i % 3 == 0 or i % 5 == 0:
#             flag = 0
#         else:
#             flag = 1
#             break

# if flag == 0:
#     print('APPROVED')
# else:
#     print('DENIED')


# C WA
# n = int(input())

# lis = []

# for _ in range(n):
#     lis.append(input())

# dic = {}
# for i in lis:
#     dic[i] = 0

# for e in lis:
#     dic[e] += 1


# print(dic)

# print('---------------------')
# max_list = [e[0] for e in dic.items() if e[1] == max(dic.values())]
# for i in reversed(max_list):
#     print(i)

# D TLE
import itertools

n, k = map(int, input().split())
lis = list(map(int, input().split()))

lis3 = []
for i in list(itertools.combinations(lis, 2)):
    lis3.append(i[0] * i[1])

print(sorted(lis3)[k - 1])