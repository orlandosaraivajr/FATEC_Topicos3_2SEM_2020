lista = [1,2,'feijão','arroz',3,4,'feijão no prato']

for item in lista:
    if type(item) is str:
        print(item.upper())

for item in lista:
    if isinstance(item, str):
        print(item.upper())

for item in lista:
    try:
        print(item.upper())
    except AttributeError:
        pass


print(list(map(lambda x: x.upper(), filter(lambda x: isinstance(x, str), lista))))

# Uso de tuplas - tipo imutável
posicao1 = (13121, 54212)
posicao2 = (3121, 4212)
gps = [posicao1, posicao2]

# range
for x in range(10):
    print(x)
