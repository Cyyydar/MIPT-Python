import random

numbers = []

for _ in range(20):
    numbers.append(random.randint(0, 100))

print("Исходный массив:")
print(numbers)

hist = [""] * 10

for num in numbers:
    if num!=100:
        hist[num//10]+="■"
    else:
        hist[-1]+="■"

for i in range(len(hist)):
    print(f"{i+1}-й бин: {hist[i]} \t Вероятность", len(hist[i])/20)