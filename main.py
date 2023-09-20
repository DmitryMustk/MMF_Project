def Interpol1(x, y, N, f):
    for i in range(N):
        if f >= x[i] and f <= x[i + 1]:
            return y[i] + (y[i + 1] - y[i]) * (f - x[i]) / (x[i + 1] - x[i])


def Interpol2(x, y, N, f):
    l = [0] * 1000
    s = 0

    for i in range(N + 1):
        p = 1
        for j in range(N + 1):
            if j != i:
                p = p * (f - x[j]) / (x[i] - x[j])
        l[i] = p

    for i in range(N + 1):
        s = s + y[i] * l[i]

    return s


n = int(input())
X = []
Y = []
F = 0

for i in range(n):
    args = [float(i) for i in input().split()]
    X.append(args[0])
    Y.append(args[1])
F = float(input())

print(Interpol1(X, Y, n, F))
#print(Interpol2(X, Y, n, F))
