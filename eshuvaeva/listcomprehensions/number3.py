print([j[0][0] for j in zip(enumerate([m for m in (list(map(str, input().split())))]),enumerate([g for g in (list(map(str, input().split())))])) if j[0][1] == j[1][1]])