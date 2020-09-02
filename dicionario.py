lista_telefonica = {}
lista_telefonica['Orlando'] = ['Orlando Saraiva','Rio Claro']
lista_telefonica['marcelo'] = ['Marcelo','Araras']
lista_telefonica['andre'] = ['André','Araras']
lista_telefonica['xyz'] = 'Teste'
lista_telefonica['xy'] = 15

try:
    print(lista_telefonica['orlando'])
except KeyError:
    print(0)

try:
    print(lista_telefonica['Orlando'])
except KeyError:
    print(0)


print(lista_telefonica.get('Orlando',0))
print(lista_telefonica.get('orlando',0))

print('marcelo' in list(lista_telefonica))
print('Marcelo' in list(lista_telefonica))