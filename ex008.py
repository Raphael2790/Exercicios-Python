d = float(input("Uma distância em metros:"))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000

print(f"A medida de {d:.1f} corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm")
