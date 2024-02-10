potencia = 5**2
potenciaFuncBuiltIn = pow(5, 2)
raizQuadrada = 81**(1/2)
raizCubica = 127**(1/3)
concatenacao = "Olá " + "Mundo!"
repeticao = "="*20 # Resultado será '==================='

nome = input("Qual seu nome?")
# Escreve com 20 caracteres caso nome não tenha a quantidade completa com espaços
print(f"Prazer em te conhecer {nome:20}!")

# Alinha no começo
print(f"Prazer em te conhecer {nome:<20}!")

# Alinha no final
print(f"Prazer em te conhecer {nome:>20}!")

# Alinha no meio
print(f"Prazer em te conhecer {nome:^20}!")

# Alinha no meio e completa com caracter especificado
print(f"Prazer em te conhecer {nome:=^20}!")

n1 = int(input("Um valor:"))
n2 = int(input("Outro valor:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Sobrescreve o end default e formata o float pata apenas 3 casas apos a virgula
print(f"A soma é {s}, o produto é {m} e a divisão é {d:.3f}", end=" ")
print(f"A divisão inteira é {di} e potência {e}")
