n = int(input())

for i in range(n):
    ans = "yes"
    ar = input().split()
    k = ar[3]
    for j in range(3):
        if ar[j] != k:
            ans = "no"
    print(ans)