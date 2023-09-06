n = int(input("Informe um número inteiro de 3 dígitos: "))

c = n // 100
resto =  n % 100
d = resto // 10
u = resto % 10

n = u * 100 + d * 10 + c

print(f"{n}")
