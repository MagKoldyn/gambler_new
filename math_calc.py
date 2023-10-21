def getHwostik(ostatok):
    if ostatok >= 10:
        # Д3
        return 4
    elif ostatok >= 8:
        # К2
        return 3
    elif ostatok >= 5:
        # Д2
        return 2
    elif ostatok >= 2:
        # Д1
        return 1
    else:
        # К1
        return 0


N = int(input("Введите N"))
t1 = (N - 13) // 13 * 5 + 5 + getHwostik(N % 13)
t2 = t1
t3 = N - (t1 + t2)
t = [t1, t2, t3]
print(t)
