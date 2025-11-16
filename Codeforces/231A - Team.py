n = int(input())
total = 0
for i in range(n):
    ar = input().split()
    if ar.count("1") >= 2:
        total += 1
print(total)