for i in range(174457,174506):
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k+=1
    if k == 2:
        for j in range(2, i):
            if i % j == 0:
                print(j)