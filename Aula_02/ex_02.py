print("Informe o número do mês: ")
x = int(input())
while x > 12 or x < 1:
    print("valor incorreto, informe o número do mês: ")
    x = int(input())

mes = ""
trimestre = ""

if 1 <= x <= 3:
    trimestre = "primeiro"
    if x == 1:
        mes = "janeiro"
    elif x == 2:
        mes = "fevereiro"
    elif x == 3:
        mes = "março"

elif 4 <= x <= 6:
    trimestre = "segundo"
    if x == 4:
        mes = "abril"
    elif x == 5:
        mes = "maio"
    elif x == 6:
        mes = "junho"

elif 7 <= x <= 9:
    trimestre = "terceiro"
    if x == 7:
        mes = "julho"
    elif x == 8:
        mes = "agosto"
    elif x == 9:
        mes = "setembro"

elif 10 <= x <= 12:
    trimestre = "quarto"
    if x == 10:
        mes = "outubro"
    elif x == 11:
        mes = "novembro"
    elif x == 12:
        mes = "dezembro"

print("O mês de", mes, "é do", trimestre, "trimestre do ano")