for i in range(190201, 190260):
    n = 0
    dels = []
    for j in range(2, i+1, 2):
        if i % j == 0:
            n += 1
            dels.append(j)
            if n > 4:
                break
    if n == 4:
        print(i, dels[-1], dels[-2])
#  Ответ:
# 190226 190226 838
# 190234 190234 17294
# 190238 190238 2606
# 190252 190252 95126
# 190258 190258 758