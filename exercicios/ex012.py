preco = float(input("Qual o preço do produto? R$"))
desconto = preco * (5/100)
precoComDesconto = preco - desconto
print(f"O preço que custava R${preco:.2f}, na promoção com deconto de 5% vai custar R${precoComDesconto:.2f}.\nO "
      f"desconto aplicado foi de R${desconto:.2f}")
