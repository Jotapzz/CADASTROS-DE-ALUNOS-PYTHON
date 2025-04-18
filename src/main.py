from Alunos import Alunos
import time
import os


#Função para Limpar a tela
def limpar_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)


#Lista dos Alunos Cadastrado
lista_Alunos = []

while True:
    limpar_tela()

    #Imprimindo o Menu
    print('===== CADASTRO DE ALUNOS =====')
    print('Escolha uma opção a seguir...')
    time.sleep(2)
    print('1 - Adicionar Alunos')
    print('2 - Verifica Alunos Cadastrado')
    print('3 - Sair')
        

    try:
        opcao = int(input('Escolha uma Opção: '))

    except ValueError:
        limpar_tela()
        print('Digite um Valor Correto')
        time.sleep(1)
        continue

    if opcao == 1:

            #Tratamento de Erro ao Cadastrar aluno
            try:
                nome, idade = Alunos.cadastroAlunos() #Pega o retorno da função
                aluno = { #Transforma em Dicionario
                'Aluno': nome,
                'Idade': idade
                }
                # e Coloca o Dicionario em uma Array
                lista_Alunos.append(aluno)
            except:
                print()

            time.sleep(2)


    elif opcao == 2:
            limpar_tela()
            print('==== LISTA DE ALUNOS CADASTRADO ====')

            # Amostra todos os dados dos Alunos Cadastrado
            for aluno in lista_Alunos:
                    print (f'Nome:{aluno['Aluno']}   Idade: {aluno['Idade']}')

            time.sleep(4)

    elif opcao == 3:
            print('Até mais...')
            time.sleep(1)
            break #Sai do Loop

    else:
            print('Não Existe Essa Opção!')
