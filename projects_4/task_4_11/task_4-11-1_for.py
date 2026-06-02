a = [1, 2, 3]
b = [4, 5, 6]
scalar = 0
for i in range(len(a)):
    scalar = scalar + a[i] * b[i]
print("Скалярное произведение двух векторов:", scalar)