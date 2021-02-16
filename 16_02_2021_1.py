for i in range(164700, 164753):
    n = 0
    dels = []
    for j in range(1, i+1):
        if i % j == 0:
            n += 1
            dels.append(j)
            if n > 6:
                break
    if n == 6:
        print(i, dels[-2], dels[-1])
#   Ответ
# 164708 82354 164708
# 164709 54903 164709
# 164716 82358 164716
# 164732 82366 164732