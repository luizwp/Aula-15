class car:
    def __init__(self, c, ma, mo):
        self.cor = c
        self.marca = ma
        self.modelo = mo
        self.velocidade_atual = 0


def acelerar(self):
    self.velocidade_atual += 20
    print(f'Acelerando... Velocidade: {self.velocidade_atual}')

car1 = car('azul', 'chevrolet', 2016)
print(car1.modelo, car1.marca, car1.cor)

