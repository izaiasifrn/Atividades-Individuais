# LOCADORA DE VEICULOS
class ErroDeLocadora(Exception):
    pass

class VeiculoNaoEncontradoError(ErroDeLocadora):
    pass

class VeiculoIndisponivelError(ErroDeLocadora):
    pass

class Veiculo:
    def __init__(self, placa: str, modelo: str, valor_diaria: float, disponivel: bool = True) -> None:
        self.placa = placa
        self.modelo = modelo
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def __eq__(self, other:object) -> bool:
        if not isinstance(other, Veiculo):
            return NotImplemented
        return self.placa == other.placa

    def __str__(self) -> str:
        return f"Placa: {self.placa} | Modelo: {self.modelo} | Valor da diária: {self.valor_diaria} | Disponibilidade: {self.disponivel}"

    @classmethod
    def a_partir_de_texto(cls, texto: str) -> "Veiculo":
        # texto.split("|")
        # partes = [texto[0], texto[1], texto[2]]
        # placa = partes[0]
        # modelo = partes[1]
        # valor = partes[2]

        # return cls(placa, modelo, valor)
        partes = texto.split("|")
        placa = partes[0]
        modelo = partes[1]
        valor = float(partes[2])

        return cls(placa, modelo, valor)

    @staticmethod
    def placa_valida(placa: str) -> bool:
        return len(placa) == 7

    @property
    def valor_diaria(self) -> float:
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor: float) -> None:
        if valor < 0:
            raise ValueError(valor)
        self._valor_diaria = valor

class Locadora:
    def __init__(self) -> None:
        self._acervo: list[Veiculo] = []

    def cadastrar(self, veiculo: Veiculo) -> None:
        self._acervo.append(veiculo)

    def _buscar(self, placa: str) -> Veiculo:
        for veiculo in self._acervo:
            if veiculo.placa == placa:
                return veiculo
        raise VeiculoNaoEncontradoError(placa)

    def alugar(self, placa: str) -> None:
        veiculo = self._buscar(placa)
        if not veiculo.disponivel:
            raise VeiculoIndisponivelError(placa)
        veiculo.disponivel = False

    def devolver(self, placa: str) -> None:
        self._buscar(placa).disponivel = True

    def disponiveis(self) -> list[Veiculo]:
        disponibilidade = []
        for veiculo in self._acervo:
            if veiculo.disponivel:
                disponibilidade.append(veiculo)
        return disponibilidade

locadora = Locadora()
carro1 = Veiculo("6342537", "Toyota Corolla", 130.0)
locadora.cadastrar(carro1)

carro2 = Veiculo("6390537", "Toyota Corolla", 130.0)
locadora.cadastrar(carro2)

locadora.alugar("6342537")

try:
     locadora.alugar("6342537")  
except VeiculoIndisponivelError as erro:
    print(f"Operação negada: {erro} já está alugado.")
except VeiculoNaoEncontradoError as erro:
    print(f"Operação negada: {erro} não foi encontrado na locadora.")

for veiculo in locadora.disponiveis():
        print(veiculo)  



# CONTA BANCARIA REFORCANDO O PROPERTY E SETTER
class SaldoNaoPodeSerNegativoError(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo: float) -> None:
        self.saldo = saldo

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        if saldo < 0:
            raise SaldoNaoPodeSerNegativoError(saldo)
        self._saldo = saldo



# QUADRADO
class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura 

    @classmethod
    def quadrado(cls, lado: float) -> "Retangulo":
        return cls(lado, lado)

    @staticmethod
    def eh_area_valida(area: float) -> bool:
        return area > 0

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @staticmethod
    def eh_maior_de_idade(idade: int) -> bool:
        return idade >= 18

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @classmethod
    def com_bonus(cls, nome: str, salario_base: float) -> "Funcionario":
        salario_com_bonus = salario_base + (salario_base / 10)
        return cls(nome, salario_com_bonus)

class Temperatura:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @classmethod
    def de_fahrenheit(cls, fahrenheit: float) -> "Temperatura":
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)



#USO DE EQ, ISINSTANCE E NOTIMPLEMENTED
class Ponto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ponto):
            return NotImplemented
        return self.x == other.x and self.y == other.y

