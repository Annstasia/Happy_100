for i in range(174457, 174506):
    n = 0
    dels = []
    for j in range(1, i+1):
        if i % j == 0:
            n += 1
            dels.append(j)
            if n > 4:
                break
    if n == 4:
        print(dels[-3], dels[-2])


# Ответ:
# 3 58153
# 7 24923
# 59 2957
# 13 13421
# 149 1171
# 5 34897
# 211 827
# 2 87251
