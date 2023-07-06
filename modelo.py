class Filme:
    def __init__(self,nome,ano,duracao):
        self.__nome = nome
        self.__ano = ano
        self.__duracao = duracao
    @property
    def nome(self):
        return self.__nome
    @property
    def ano(self):
        return self.__ano
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self,horas):
        self.__duracao = horas



class Serie:
    def __init__(self,nome,ano,temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada


vingadores = Filme('vigandores - guerra infinita',2018,160)
atlanta = Serie('atlanta',2018,2)

vingadores.duracao ="2 horas e 40 minutos"

print(f"o filme  {vingadores.nome}  foi lançado no ano {vingadores.ano} e tem a duraçaõ de {vingadores.duracao}")
print(f"a serie {atlanta.nome} foi lançada no ano {atlanta.ano}, com duração de {atlanta.temporada} temporadas")



