import random

data = [random.randint(-10, 10) for _ in range(10)]
kernel = [1,0,-1]
k_mid = len(kernel)//2

result = []

for i in range(len(data)):
    s = 0
    for j in range(len(kernel)):
        idx = i + j - k_mid
        if 0 <= idx < len(data):
            s += data[idx] * kernel[j]
    result.append(s)
        
print("Исходный массив")
print(data)
print("Результат")
print(result)
            

