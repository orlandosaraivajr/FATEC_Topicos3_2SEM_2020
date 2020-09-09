class Cliente:
    def __init__(self, *args, **kwarg):
        self.name = kwarg.get("name", "")
        self.idade = kwarg.get("idade", 0)
        self.npedido = kwarg.get("pedido", 0)


fila_normal = []
fila_pref = []


def inserir_cli(name, idade, **npedido):
    if idade <= 65:
        fila_normal.append(Cliente(name=name, idade=idade,
                                   npedido=npedido.get("npedido", None)))
    else:
        fila_pref.append(Cliente(name=name, idade=idade,
                                 npedido=npedido.get("npedido", None)))


inserir_cli(name="Marcelo", idade=49, npedido=23)
inserir_cli(name="Eitor", idade=18)
inserir_cli(name="Maria", idade=68)

for cliente in fila_pref:
    print(cliente.name)

for cliente in fila_normal:
    print(cliente.name)
