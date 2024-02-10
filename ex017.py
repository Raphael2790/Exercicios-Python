from math import hypot, pow, sqrt

oposto = float(input("Comprimento do cateto oposto:"))
adjacente = float(input("Comprimento do cateto adjacente:"))
hipotenusa = hypot(oposto, adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")

hipotenusa_formula = ((oposto**2) + (adjacente**2))**(1/2)

hipotenusa_formula_math = sqrt((pow(oposto, 2) + pow(adjacente, 2)))

print(f"A hipotenusa vai medir seguindo a formula {hipotenusa_formula_math:.2f}")
