palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist:
            palindromelist.append(a)
palindromelist.sort()
length = len(palindromelist)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in range(length - 1, -1, -1):
            if palindromelist[i] < a:
                print(palindromelist[i])
                break
