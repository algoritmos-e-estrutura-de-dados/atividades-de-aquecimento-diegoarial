print("Informe 3 números: ")
n = input().split(" ")
n1, n2, n3 = n

MaiorAB = (int(n1) + int(n2) + abs(int(n1) - int(n2))) / 2
MaiorAC = (int(MaiorAB) + int(n3) + abs(int(MaiorAB) - int(n3))) / 2

print(f"{MaiorAC} eh o maior")