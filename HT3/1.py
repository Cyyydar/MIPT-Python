def multiplyTable(base: int):
    for i in range(1,10):
        print(f"{base} * {i} = {base * i}")

def divideTable(base: int):
    for i in range(1,10):
        print(f"{base} / {i} = {base / i}")

def minusTable(base: int):
    for i in range(1,10):
        print(f"{base} - {i} = {base - i}")

def plusTable(base: int):
    for i in range(1,10):
        print(f"{base} + {i} = {base + i}")

multiplyTable(2)
divideTable(7)
minusTable(1)
plusTable(5)