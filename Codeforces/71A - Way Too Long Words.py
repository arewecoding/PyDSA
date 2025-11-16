n = input()

for i in range(int(n)):
    ch = input()
    if len(ch) <= 10:
        print(ch)
    else:
        print(ch[0], len(ch) - 2, ch[-1], sep="")