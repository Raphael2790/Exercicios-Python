largura = float(input("Largura da parede:"))
altura = float(input("Altura da parede:"))
litrosTintaPorMetroQuadrado = 2.0
area = largura * altura

print(f"Sua parede tem a dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.3f}m².")
print(f"para pintar essa parede, você precisará de {(area/litrosTintaPorMetroQuadrado)}l de tinta.")
