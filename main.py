print("Введите число: ")
x = int(input())
print("Чётные числа: ", end="")
for i in range(2,x,2):
    print(f"{i}", end=" ")