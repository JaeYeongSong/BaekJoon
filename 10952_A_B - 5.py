while True:
    a = input().split()
    a = list(map(int, a))
    if a[0] == 0 and a[1] == 0:
        break
    print(a[0] + a[1])