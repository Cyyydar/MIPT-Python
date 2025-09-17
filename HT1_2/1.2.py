
a = 1
for i in range(5):
    for j in range(5):
        if not (i + j) % 2:
            print("*", end="\t")
        else:
            print(a, end="\t")
            a += 1
    print("")