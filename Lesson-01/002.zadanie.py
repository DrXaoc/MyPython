import time
T = int(input('Введите секунды: '))
print(time.strftime('%H:%M:%S', time.gmtime(T)))