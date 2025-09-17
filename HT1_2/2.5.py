import random

list = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список")
print(list)

outlist = list.copy()
for i in range(len(list)):
    if list[i] < 0:
        r = 0
        l = 0
        for j in range(i-1, -1, -1):
            if list[j] > 0:
                l = list[j]
                break
        for j in range(i+1, len(list)):
            if list[j] > 0:
                r = list[j]
                break
        outlist[i] = (r + l)//2
print("Выходной список")
print(outlist)