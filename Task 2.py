n, k = (int(input("Введите количество человек: ")),
int(input("Введите количество какой по счету человек выбывает: ")))
last = 0
for i in range(1, n + 1):
    last = (last + k) % i
print ("Номер человека, который останется в кругу последним: ", (last + 1))