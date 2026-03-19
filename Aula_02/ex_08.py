s = input("Digite uma frase: ")
for i in range(len(s)):
    s = s[1:] + s[0]
    print(s)
          