def diagonalDifference(arr):

    count = 0
    count_1 = 0

    Len = len(arr)

    for i in range(Len):
        for j in range(Len, -1, -1):
            print(j)
            if (i+j == Len-1):
                count = count + arr[i][j]
            if (i == j):
                count_1 = count_1 + arr[i][j]

    return abs(count - count_1)
