print("Digite quatro valores inteiros: ")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

while a == b or a == c or a == d or b == a or b == c or b == d or d == c:
    print("Sem números iguais, digite quatros valores inteiros: ")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

print("Maior valor = ", max(a, b, c, d))
print("menor valor = ", min(a, b, c, d))