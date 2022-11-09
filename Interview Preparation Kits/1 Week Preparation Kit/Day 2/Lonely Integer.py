def lonelyinteger(a):
    result = 0
    duplicate_list = list()
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i] == a[j] and i != j):
                duplicate_list.append(a[i])

    for i in a:
        if (i not in duplicate_list):
            result = i

    return result
