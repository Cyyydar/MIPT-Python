import random

def vec_norm(vec):
    res = []
    for elem in vec:
        res.append(elem**2)
    return sum(res)**(1/2)

N = int(input("Введите размерность векторов: "))
scalar = int(input("Введите скаляр для умножения: "))

vec1 = [random.randint(-10, 10) for _ in range(N)]
vec2 = [random.randint(-10, 10) for _ in range(N)]
print("Вектор 1: \n",vec1)
print("Вектор 2: \n",vec2)


sum_vec = [0]*N
mul_vec = sum_vec.copy()

for i in range(N):
    sum_vec[i]=vec1[i]+vec2[i]
    mul_vec[i]=vec1[i]*vec2[i]

print("Сумма: \n", sum_vec)
print("Умножение: \n", mul_vec)

m_vec = []

if vec_norm(vec1) > vec_norm(vec2):
    m_vec = vec1
    print("У вектора 1 бОльшая норма")
else:
    m_vec = vec2
    print("У вектора 2 бОльшая норма")

for i in range(N):
    m_vec[i]*=scalar
print("Результат умножения на скаляр:\n", m_vec)