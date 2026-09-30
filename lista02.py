#1º a variavel com um underscore é apenas uma especie de acordo social entre os desenvolvedores para dizer que ninguem deve mecher naquilo de fora, sendo assim privado, já com dois underscores é para que nao dê problema de hierarquia de herança entre classe mae e filha 

#2º vai dar um erro de atributo pois sem o setter, nao existe nenhum mecanismo de escrita configurado para o nome total

#3º porque a validação no setter é sempre cumprida independente do modulo onde o atributo for importado, ja sem ele sempre terá que fazer a validacao todas as vezes que importar, o que pode gerar problemas

#4º Alem desse Exception pegar qualquer tipo de erro, sendo assim genérico e nao especifica qual foi o erro em si, mesmo que o erro seja esperado do dominio (classificado por quem programou o programa) ou um bug normal despercebido como um AtributeError, o pass garante que mesmo capturando, nada vai ser feito com o erro, nem sequer ser apresentado.

#5º MeuErro herda o comportamento de exception, a mae de quase todas as exceções do python, onde esse comportamento é guardar uma mensagem e mostrar resumidamente entre outros comportamentos

#Cadastro com Validacao
class ErroDeSalario(Exception):
    pass

class SalarioInvalidoError(ErroDeSalario):
    pass

class Funcionario:
    #constante para servir como base na comparacao do setter
    SALARIO_MINIMO = 1518.0

    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario 

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float) -> None:
        if valor < self.SALARIO_MINIMO:
            raise SalarioInvalidoError(valor)
        self._salario = valor

    #metodo para aumentar o percentual
    def aumentar(self, percentual: int) -> None:
        if not (0 < percentual <= 30):
            raise ValueError(percentual)
        self.salario = self.salario + (self.salario * (percentual / 100))

try:
    funcionario1 = Funcionario("Izaias", 1519.0)
    funcionario1.aumentar(20)
except ValueError as erro:
    print(f"Operação negada: {erro} não é um valor aceito como percentual.")
except SalarioInvalidoError as erro:
    print(f"Operação negada: {erro} é menor do que um salario minimo")


# Cadastrar emails

#regras: ter @ e . no endereco se nao vai dar erro
# dados: endereco do email

class ErroDeEmail(Exception):
    pass

class EmailInvalidoError(ErroDeEmail):
    pass

class Email:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco

    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        if not ("@" in endereco and "." in endereco):
            raise EmailInvalidoError(endereco)
        self._endereco = endereco

try:
    email = Email("IzaiasRodriguesDantas.gmailcom")
except ErroDeEmail as erro:
    print(f"Operacao negada: {erro} não apresenta '@' e/ou '.'")
