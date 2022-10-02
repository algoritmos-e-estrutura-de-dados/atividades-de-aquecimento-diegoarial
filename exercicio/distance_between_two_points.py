import math
print("Informe a localização X1 e Y1, respectivamente: ")
P1 = input().split(" ")
print("Informe a localização X2 e Y2, respectivamente: ")
P2 = input().split(" ")
X1, Y1 = P1
X2, Y2 = P2

D = math.sqrt(pow(float(X2) - float(X1),2) + pow(float(Y2) - float(Y1),2))

print(f"{D: .4f}")