# criação da classe pessoa
class Pessoa:
    olhos = 2 #atributo defautl ou atributo de classe

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    #criação do método
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod #decorator
    def metodo_estatico():
        return  42

    @classmethod
    def nome_e_atributos_de_classe(cls):   #cls alusão palavra class (Pessoa)
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):   #classe Homem herda todos os atributos e métodos da classe pai Pessoa
    pass




if __name__ =='__main__':
    renzo = Homem(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))

