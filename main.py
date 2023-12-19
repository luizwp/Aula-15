class Funcionario:
    # método construtor
    def __init__(self, n, i, s):
        self.nome = n
        self.idade = i
        self.salario = s
        self.qtd_faltas = 0
       # print(f'Nome do funcionario criado: {self.nome}')

    def atribuirFalta(self):
        self.qtd_faltas += 1
        print(f'Falta atribuida. Quantidade: {self. qtd_faltas}')

    def aumentarsalario(self, aumento):
        self.salario += aumento


funcio1 = Funcionario('Jonas', 18, 1500)
funcio2 = Funcionario('Leticia', 18, 2100)
funcio1.aumentarsalario(300)
funcio1.atribuirFalta()
funcio1.atribuirFalta()
funcio2.atribuirFalta()
print(funcio1.qtd_faltas)
print(funcio2.qtd_faltas)

# print(funcio1.nome)
# funcio1.nome = 'Jonas Lopes'
# print(funcio1)











