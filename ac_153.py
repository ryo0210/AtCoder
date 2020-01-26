# A--------------------------------------
# h, a = map(int, input().split())

# num = 0
# while(1):
#     num += 1
#     h -= a
#     if h <= 0:
#         print(num)
#         break


#B--------------------------------------

# h, n = map(int, input().split())
# a = list(map(int, input().split()))

# a.sort(reverse=True)
# if h - sum(a) <= 0:
#     print('Yes')
# else:
#     print('No')


# C--------------------------------------
# import sys

# sys.setrecursionlimit(10**9)

# h, k = map(int, input().split())
# hi = list(map(int, input().split()))
# hi.sort(reverse=True)
# del hi[:k]

# num = 0
# if hi == []:
#     print(0)
# else:
#     for i in hi:
#         num += i
#     print(num)


# D--------------------------------------
# h = int(input())

# num = 0
# while(1):
#     num += 1
#     h = h // 2
#     if h < 1:
#         break

# print(2 ** num - 1)


# E--------------------------------------
# 時間が無くて焦って、コスパだけで考えてしまった。
# 体力が残り少ない敵に対しても、魔力消費量が多くてもコスパの良い魔法を使うプログラムになってしまった。
# 完全に運だが、初めてE問題まで行けた。

magic = []
h, n = map(int, input().split())
for _ in range(n):
    magic.append(list(map(int, (input().split()))))

cost_performance = []
for i, e in enumerate(magic):
    cost_performance.append(float(magic[i][1]) / float(magic[i][0]))

min_cost = cost_performance.index(min(cost_performance))

num = 0
magic_cost = 0
while(1):
    num =+ 1
    magic_cost =+ magic[min_cost][1]
    h -= magic[min_cost][0]
    print(magic_cost)
    print(h)
    print('______________')
    if h < 1:
        break

print(magic_cost)
