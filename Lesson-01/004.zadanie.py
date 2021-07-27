X = int(input('введите целое положительное число:'))
Y = 0
while X>0:
    if X%10>Y:
       Y = X%10
    X = X//10
print(Y)

