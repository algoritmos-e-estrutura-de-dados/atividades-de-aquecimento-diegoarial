N = input("Informe o nome do assalariado: ")
SF = input("Informe o salário fixo: ")
B = input("Informe o valor total do que vendeu no mês: ")

x = (float(B) * 0.15)
t = (float(x) + float(SF))

print(f"TOTAL = R$ {t: .2f}")