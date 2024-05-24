string = 'Raphael'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe o atributo {metodo}')

    # Uma oportunidade para invocar metodos em classes especializadas usando classes base?
    print(getattr(string, metodo)())
    