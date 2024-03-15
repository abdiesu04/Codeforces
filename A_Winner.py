n = int(input())
scores = {}
order = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if name not in scores:
        scores[name] = score
        order.append((name, score))
    else:
        scores[name] += score
        order.append((name, scores[name]))

max_score = max(scores.values())
winners = [name for name, score in scores.items() if score == max_score]

for name, score in order:
    if name in winners and score >= max_score:
        print(name)
        break