for i in range(194455, 194500):
    n = 0
    dels = []
    for j in range(1, i+1):
        if i % j == 0:
            n += 1
            dels.append(j)
            if n > 4:
                break
    if n == 4:
        print(i, dels[-2], dels[-1])

# Ответ
# 194455 38891 194455
# 194459 1193 194459
# 194461 1399 194461
# 194462 97231 194462
# 194473 1721 194473
# 194477 443 194477
# 194482 97241 194482
# 194489 4523 194489
# 194491 17681 194491
