class Funcionario:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def exibirDados(self):
        print('Dados do funcionário')
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

class Monitor(Funcionario):
    def __init__(self, matricula, nome, idade, cargaHoraria):
        super().__init__(matricula, nome, idade)


        def exibirDados(self):
            super().exibirDados()
            print(f'Carga Horaria: {self.cargaHoraria}')

    class Professor(Funcionario):
    def __init__(self, matricula, nome, idade, turma):
        super().__init__(matricula, nome, idade)
        self.turma = turma
class Coordenador(Funcionario):
    pass

m1 = Monitor(1, 'Jonas', 18, 300)
m1.exibirDados()
