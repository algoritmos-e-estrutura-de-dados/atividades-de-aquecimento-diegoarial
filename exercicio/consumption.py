X = input("Informe o total de KM que o automóvel já percorreu: ")
Y = input("Informe o total de combustível gasto: ")

T = (int(X) / float(Y))

print(f"{T: .3f} km/l")