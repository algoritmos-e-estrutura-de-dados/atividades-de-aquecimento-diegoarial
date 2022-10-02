N = input("Informe o número de empregado: ")
H = input("Informe o número de horas trabalhadas no mês: ")
PH = input("Informe o valor que recebe por hora trabalhada: ")

s = (int(H) * float(PH))

print(f"NUMBER = {N}")
print(f"SALARY = U$ {s: .2f}")