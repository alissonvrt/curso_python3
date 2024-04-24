# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

# Checagem, ser um item da lista e uma instancia de set
for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    # checar ser o item da lista e uma instancia de str
    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    # Checar ser um item da lista e uma instancia de int ou float
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    # Checagem final para saber ser um item não é nem um dos outros acima    
    else:
        print('OUTRO')
        print(item)