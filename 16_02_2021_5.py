count = 0
for i in range(3532000, 3532161):
    n = 0
    # dels = []
    for j in range(1, i+1):
        if i % j == 0:
            n += 1
            # dels.append(j)
            if n > 2:
                break
    if n == 2:
        count+=1
        print(count, i)

# Ответ:
# 1 3532007
# 2 3532019
# 3 3532021
# 4 3532033
# 5 3532049
# 6 3532091
# 7 3532103
# 8 3532121
# 9 3532147