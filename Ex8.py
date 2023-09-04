nome = str(input("Coloque seu nome"))
vendas = int(input("Quantos carros foram vendidos"))
valor = float(input("Valor total das vendas"))

comissao = 200 * vendas
salario = 2500
porcentagem = valor * 0.02

print(f'Você gamhará: {salario + comissao + porcentagem}')
