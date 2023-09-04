numero = int(input("digite uma centena"))

centena = numero // 100
dezena =  numero % 100
unidade = numero / 10

print(f"{unidade,dezena,centena}")
