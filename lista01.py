#Questão 1
class aluno:
    def __init__(self, nome:str, matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def lancar_nota(self, valor:float):
        self.valor = valor
        self.notas.append(valor)

    def media(self) -> float:
        notas_acumulador = 0
        notas_contador = 0
        for nota in self.notas:
            notas_acumulador += nota
            notas_contador += 1
        return notas_acumulador / notas_contador

    def aprovado(self) -> bool:
        return self.media() >= 6

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - média {self.media()}"



aluno1 = aluno("Izaias", "20261148060012")
aluno1.lancar_nota(8)
aluno1.lancar_nota(3)
aluno2 = aluno("Joao", "20261148060039")
aluno2.lancar_nota(8)
aluno2.lancar_nota(8)
aluno3 = aluno("Carlos", "20261148060097")
aluno3.lancar_nota(8)
aluno3.lancar_nota(3)

alunos = [
    aluno1, aluno2, aluno3
]

for a in alunos:
    if a.aprovado():
        print(a)


    
#Questão2

class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)

    def __eq__(self, value):
        return self.base == value.base and self.altura == value.altura

class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto):
        dia, mes, ano = texto.split("/")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        return cls(dia, mes, ano)

    @staticmethod
    def bissexto(ano: int) -> bool:
        return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
        

    
