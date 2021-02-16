for i in range(190061, 190073):
    n = 0
    dels = []
    for j in range(1, i+1, 2):
        if i % j == 0:
            n += 1
            dels.append(j)
            if n > 4:
                break
    if n == 4:
        print(i, dels[-1], dels[-2])

# Ответ:
# 190061 190061 6131
# 190064 11879 1697
# 190067 190067 2677
# 190072 23759 1033
