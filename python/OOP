class Carro:
    def __init__(self, modelo, cor, a_venda, ano):
        self.modelo = modelo
        self.cor = cor
        self.a_venda = a_venda
        self.ano = ano

    def acelerou(self):
        print(f"Voce acelerou o carro {self.modelo} {self.cor} do ano de {self.ano}")
       
    def parou(self):
        print(f"Voce parou o carro {self.modelo} {self.cor} do ano de {self.ano}")

class Estudante:

    class_ano = 2020 # toda instância compartilha o mesmo valor, a menos que você mude manualmente. como se fosse uma global
    numero_estudante = 0

    def __init__(self, aluno, idade):
        self.aluno = aluno
        self.idade = idade
        Estudante.numero_estudante += 1 # para mudar variaveis tem que fazer isso nome da NomeClass.nomeVar 

class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.vivo = True

    def comer(self):
        print(f"{self.nome} precisa comer")

    def dormir(self):
        print(f"{self.nome} precisa dormir")

# as coisas dentro do (coisa) vao ser as heranças mesmo com o pass, se add coisa em alguma class que ja recebeu herança ela conta pra ela mesma
class Cachorro(Animal): 
    pass

class Gato(Animal):
    pass

class Rato(Animal):
    pass




#-----------------------------CLASS---------------------------
# from oop import Carro
# #para chamr isso voce tem que criar uma varivele com o nome da class e seus parametros

# carro1 = Carro("BMW", "VERMELHO", True, 2007)
# carro2 = Carro("Mustang", "Azul", False, 2026)

# print(carro1.modelo) #printar especificamente o que vai o que voce digitou la dos parametros do __init__
# print(carro1.a_venda)
# print(carro1.cor)
# print(carro1.ano)

# print(carro2.modelo) 
# print(carro2.a_venda)
# print(carro2.cor)
# print(carro2.ano)

# carro1.parou()
# carro2.acelerou()

#---------------------------CLASS VARIABLE--------------------

# from oop import Estudante   

# estudante1 = Estudante("Bob Esponja", 30)
# estudante2 = Estudante("Patricka", 35)

# print(estudante1.aluno)
# print(estudante1.idade)
# print(Estudante.class_ano) # a variavel ja e chamada direto da instancia sem passar por outras variaveis, ja chama direto pelo nome da class
# print(Estudante.numero_estudante)

# print(estudante2.aluno)
# print(estudante2.idade)
# print(Estudante.class_ano)
# print(Estudante.numero_estudante)

#----------------------------------INHERITANCE-------------------
from oop import Animal, Cachorro, Rato, Gato
cachorro = Cachorro("Scooby")
gato = Gato("Garfield")
rato = Rato("Mickey")
print("\n")

print(cachorro.nome)
print(cachorro.vivo)
cachorro.comer()
cachorro.dormir()

print("\n")

print(gato.nome)
print(gato.vivo)
gato.comer()
gato.dormir()

print("\n")

print(rato.nome)
print(rato.vivo)
rato.comer()
rato.dormir()
print("\n")
