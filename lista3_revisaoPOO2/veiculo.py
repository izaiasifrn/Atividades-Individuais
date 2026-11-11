from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, placa:str, diaria: float) -> None:
        self.placa = placa
        self.diaria = diaria

    @abstractmethod
    def calcular_aluguel(self, dias: float) -> float:
        pass

    def descricao(self) -> str:
        return (f"{type(self).__name__} {self.placa} | diária: {self.diaria}")

class Carro(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self, dias: float) -> float:
        return self.diaria * dias

class Moto(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self, dias: float) -> float:
        return self.diaria * dias * 0.8

class Caminhao(Veiculo):
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self, dias) -> float:
        return self.diaria * dias + 100

class Locadora:
    def __init__(self, nome_locadora: str) -> None:
        self.nome_locadora = nome_locadora
        self.veiculos = list[Veiculo] = []

    def cadastrar(self, veiculo: Veiculo) -> None:
        self.veiculos.append(veiculo)

    #polimorfismo por heranca
    def faturamento_previsto(self, dias: int) -> float:
        total = 0
        for v in self.veiculos:
            total += v.calcular_aluguel(dias)
        return total
    
    
    