a = int(input("введите расстояние в день в км>>>"))
b = int(input("введите максимальный результат в км >>>"))
c = 1
while (a + 0.1) > 0:
    a = a * (1 + 0.1)
    if a // b >= 1:
        print(c + 1)
        break
    c += 1