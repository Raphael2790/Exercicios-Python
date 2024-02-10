n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
s = int(n1) + int(n2)
tn1 = type(n1)
ts = type(s)

# Comentários no python

print(f"A soma dos números é: {s}")
print(f"Os tipos são {tn1} e {ts}")

# Converter para texto
n3 = str(233)
# Converter para boolean
n4 = bool("Olá mundo!")
# Converter para float
n5 = float(3)

if n1.isnumeric():
    print("Pode ser convertido")
else:
    print("Não pode ser convertido")
