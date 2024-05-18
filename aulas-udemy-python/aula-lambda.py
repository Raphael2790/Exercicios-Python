def executa(function, *args):
    return function(args)


l1 = [
    {'nome': 'Paulo', 'sobrenome': 'Silva'},
    {'nome': 'André', 'sobrenome': 'Tomoyo'}
]

l1.sort(key=lambda item: item['nome'])
print(l1)

print(executa(
    lambda *args: sum(*args),
    2, 12, 24
))
