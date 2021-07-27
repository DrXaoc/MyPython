x = int(input('В первый день км:'))
y = int(input('Я должен пробежать:'))
i = 1
print('1 -й день:', x)
while x < y:
    x *= 1.1
    i += 1
    print(i,'-й день:', x)