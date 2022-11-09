def lonelyinteger(a):
    count = 0
    b = list()
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i] == a[j] and i != j):
                b.append(a[i])

    for i in a:
        if (i not in b):
            count = i

    return count
