print("Digite quatros valores inteiros: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

pares = 0
impares = 0
for i in (a, b, c, d):
    if i % 2 == 0:
        pares += i

    else:
        impares += i

print("soma dos pares: ", pares)
print("soma dos impares: ", impares) 