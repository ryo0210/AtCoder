# 高橋君は500円玉をK枚持っています。
# これらの総額がX円以上である場合は'Yes'を、そうでない場合は'No'を出力してください。
'''
k, x = map(int, input().split())
money = 500 * k
if money >= x:
    print('Yes')
else:
    print('No')'''



# 英大文字のみからなる長さNの文字列Sがあります。
# の連続する部分列 (入出力例をご覧ください) として ABC がいくつ含まれるかを求めてください。
'''import re
n = int(input())
s = input()

result = re.findall(r'ABC', s)
print(len(result))'''

# 大きさNの順列((1,2,...,N)を並び替えてできる数列)P,Qがあります。
# 大きさNの順列はN!通り考えられます。
# このうち、Pが辞書順でa番目に小さく、Qが辞書順でb番目に小さいとして、|a−b|を求めてください。
import itertools
import re

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

n_list = list(range(1, n + 1))

conv =[]
for v in itertools.permutations(n_list, n):
    conv.append(v)

for i, j in enumerate(conv):
    if p == j:
        p_ind = i + 1

for i, j in enumerate(conv):
    if q == j:
        q_ind = i + 1

print(abs(p_ind - q_ind))








