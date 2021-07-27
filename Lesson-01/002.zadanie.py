Sec = int(input("Укажите время:"))
H = Sec // 3600
M = (Sec - H * 3600) // 60
S = Sec - (H * 3600 + M * 60)
print(f"{H} : {M} : {S}")