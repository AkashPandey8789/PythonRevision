l = [5, 6, 8, 92, 7, 1, 6, 41, 3, 9]


def even(n):
    for i in n:
        if i % 2 == 0:
            print(i)


even(l)

print("\n\n\n")
for i in l:
    t = lambda n: n * 2
    print(t(i))
