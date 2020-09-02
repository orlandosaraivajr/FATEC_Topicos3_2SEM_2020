def soma(num1, num2):
    return num1 + num2

assert( soma(1,2) == 3)
assert( soma('oi','mundo') == 'oimundo')
assert( soma(5.6, 6.2) == 11.8)
a = [1,2,3,4]
b = [5,6,7,8]
c = [1,2,3,4,5,6,7,8]


assert( soma(a, b) == c)
       
# Args
def soma2(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

assert( soma2(1, 2) == 3)
assert( soma2(1, 2, 3) == 6)

#kwargs
def soma3(**numeros):
    print(numeros)

def soma4(*args, **kwargs):
    print(args)
    print(kwargs)

'''
Crie uma função soma5 que realizará a soma de todos
os parâmetros passados ( seja via parâmetros nomeados ou não)
Crie testes unitários
Considere válido somente parâmetros numéricos.
'''
assert( soma5(1, 2, 3, n=2) == 8)
assert( soma5(1, 2, 3, n=[2]) == 0)
