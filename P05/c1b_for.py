n = int(input("n = "))
for i in range(n+1):
    for _ in range(i):
        print('*',end='')
    print()