# random não é uma biblioteca aleatoria utiliza internamente date time para geração
# para modificar a aleatoriedade podemos utilizar o metodo seed
import random
import time
from secrets import SystemRandom as Sr
import string as s

random.seed(time.time())

r_range = random.randrange(1, 10, 2)
print(r_range)

r_int = random.randint(1, 20)
print(r_int)

r_float = random.uniform(1, 20)
print(r_float)

nomes = ['Rapahel', 'Monica', 'Miguel']

random.shuffle(nomes)
print(nomes)

nomes_amostra = random.sample(nomes, k=2)
print(nomes_amostra)

nomes_escolhas = random.choices(nomes, k=2)
print(nomes_escolhas)

nome_escolhido = random.choice(nomes)
print(nome_escolhido)

# possui as mesmas funcionalidades do random porem sem controle da aleatoriedade
random_system = Sr()
senha = ''.join(random_system.choices(s.ascii_letters + s.digits + s.punctuation, k=12))
print(senha)
