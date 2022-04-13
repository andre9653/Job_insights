class Tupla:

    def __init__(self, keys, palavras):
        self.keys = list(keys)
        self.palavras = list(palavras)
        self.op = dict(zip(self.keys, self.palavras))

    def __getitem__(self, key):
        return self.op[key]

    def __repr__(self):
        return f'Tabela Completa: {self.op}'

    def get_tupla(self, key):
        return f'Palavra: {self.op[key]}'

    def __str__(self):
        to_print = "Key:\t| Palavra:\n"
        for item in self.op:
            to_print += str(item) + "\t  " + str(self.op.get(item)) + "\n"
        return to_print


t = Tupla(keys=(1, 2, 3, 4, 5), palavras=("um", "dois", "tres", "quatro", "cinco"))
print(t)
