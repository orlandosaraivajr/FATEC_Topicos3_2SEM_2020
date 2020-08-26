numero = int(input("Digite uma idade:   "))
if numero < 14:
    print("Menor de idade")
    print("Não pode entrar na festa")
elif numero < 18:
    print("Menor de idade")
    print("Pode entrar com autorização")
else:
    print("Maior de idade")
    print("Pode entrar")
