'''
c = input()
print(chr(ord(c) + 1))'''


'''
subjects, max_score, average = map(int, input().split())
score = list(map(int, input().split()))

total_score = 0
for s in score:
    total_score += s

if subjects * average <= total_score:
    print(0)
elif subjects * average > total_score + max_score:
    print(-1)
else:
    print(subjects * average - total_score)'''

question, submission = map(int, input().split())

results = []
for i in range(submission):
    key, result = input().split()
    if int(key) not in results:
        results[int(key)] = result
    results[int(key)].append(result)

print(results)

