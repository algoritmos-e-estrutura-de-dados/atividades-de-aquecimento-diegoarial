print("Informe respectivamente o código, quantidade e preço do produto 1: ")
linha1 = input().split(" ")
print("Informe respectivamente o código, quantidade e preço do produto 2: ")
linha2 = input().split(" ")
C1, Q1, P1 = linha1
C2, Q2, P2 = linha2

total = ((int(Q1) * float(P1)) + (int(Q2) * float(P2)))

print(f"VALOR A PAGAR: R$ {total: .2f}")