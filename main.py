def TriplesForN(N):
    N3 = [1, 1, 1]
    TriplesN = [N3]
    a2 = []

    for i in range(N - 3):
        x = TriplesN.copy()
        for Troika in x:
            for chislo in range(len(Troika)):
                Troika[chislo] = Troika[chislo] + 1
                TriplesN.append(sorted(Troika.copy())[::-1])
                Troika[chislo] = Troika[chislo] - 1
        for x in TriplesN:
            if x not in a2:
                a2.append(x)
        for z in a2.copy():
            if z[0] + z[1] + z[2] != 4 + i:
                a2.remove(z)
        TriplesN = a2
        a2 = []
        x = TriplesN.copy()
    return TriplesN


def Compare(Triple1, Triple2):
    score1 = 0
    score2 = 0
    for i in range(len(Triple1)):
        if Triple1[i] > Triple2[i]:
            score1 += 1
        elif Triple1[i] < Triple2[i]:
            score2 += 1
        else:
            score1 += 0.5
            score2 += 0.5
    if score1 > score2:
        return [1, 0]
    elif score2 > score1:
        return [0, 1]
    else:
        return [0, 0]


def DuoTriples(TriplesN):
    a = []
    for i in range(len(TriplesN) - 1):
        for j in range(i + 1, len(TriplesN)):
            a.append([TriplesN[i], TriplesN[j]])
    return a


def run(Triples):
    print("Input N")
    # print(TriplesForN)
    # print(func([[5, 1, 1], [4, 2, 1], [3, 3, 1], [3, 2, 2]]))
    Duos = DuoTriples(Triples)
    Score = {}
    for Triple in Triples:
        Score[str(Triple)] = 0
    # print(b)
    for Duo in Duos:
        c = Compare(Duo[0], Duo[1])
        Score[str(Duo[0])] += c[0]
        Score[str(Duo[1])] += c[1]
    return Score


f = open('Triple Winner', 'w')
c = []
Score = run(TriplesForN(90))
a = max(Score, key=Score.get)
print(a)
f.close()
