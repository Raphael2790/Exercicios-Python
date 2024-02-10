from math import cos, sin, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
rad = radians(angulo)
seno = sin(rad)
coseno = cos(rad)
tangente = tan(rad)
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {coseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")
