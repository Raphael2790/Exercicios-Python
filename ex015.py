precoDia = 60.00
precoKm = 0.15
dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos km rodados?"))
total = (dias * precoDia) + (km * precoKm)
print(f"O total a pagar é de R${total:.2f}")
