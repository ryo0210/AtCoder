# n, m = map(int, input().split())
# if n == m:
#     print('Yes')
# else:
#     print('No')

# a, b = map(int, input().split())
# if a >= b:
#     print(str(b) * a)
# else:
#     print(str(a) * b)

n = int(input())

nums = list(map(int, (input().split())))
print(nums)

count = 1
for i in range(1, n):
    for j in range(1, i):
        if nums[i] <= nums[j]:
            pass
        else:
            break
    
print(count)

