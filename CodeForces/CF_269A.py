# Solution to CodeForces 269A Magic Boxes
from math import ceil
from collections import defaultdict


n = int(input())  # Number of sizes
sizes = defaultdict(int)

for _ in range(n):
    k, a = map(int, input().strip().split())
    sizes[k] = a  # There are a boxes of size k


ki = 0
while True:
    # ki + 1 boxes needed to contain
    sizes[ki + 1] = max(sizes[ki + 1], ceil(sizes[ki] / 4))
    ki += 1
    if ((ki >= n) and (sizes[ki] == 1) and (ki + 1 not in sizes)):
        break

print(ki)
