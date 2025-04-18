
class Alunos:
    #Metodo Principal da Classe
    def __init__(self):
        self = self


    #Função do Cadastro dos Alunos
    def cadastroAlunos ():

        #Tratamento de Erros
        try:
            nome = str(input('Digite o nome do aluno: '))
            idade = int(input('Digite a idade do aluno: '))

            #Verificação da Idade
            if idade <=3:
                print('Infelizmente o aluno(a) é muito novo para ser Cadastrado')
            elif idade >= 100:
                print('Digite a idade do Aluno Corretamento')


            #Verificação do Nome
            elif not nome.strip() or len(nome) < 3:
                print('Digite um nome valido')

            else:
                print(f'Aluno {nome}, {idade} anos cadastrado com sucesso!')
                return nome, idade
        
        except ValueError:
            print('Erro: Digite um número Valido para Idade do Aluno!')


