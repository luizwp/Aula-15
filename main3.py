class Veiculo:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def exibirDados(self):
        print('Dados do Veiculo')
        print(f'Cor: {self.cor}')
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')


class Moto(Veiculo):
    pass


class carro(Veiculo):
    pass

m1 = Moto('preto', 'Honda', 'Biz')
m1.exibirDados()