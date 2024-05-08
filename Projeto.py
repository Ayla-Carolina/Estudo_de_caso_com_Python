agenda = [] #criando uma lista vazia 

######     Definição das funções 

#Função para novo contato na agenda 

#Nome: novo()
#Tipo: procedimento 
def novo():

    global agenda #Definindo a variável como global 
    nome = p_nome()
    celular = input("Celular....: ")
    email = input("E-mail....: ")
    agenda.append([nome, celular, email]) #adicionando os dados na agenda 

    print("""
          -------- REGISTRO GRAVADO COM SUCESSO !!!! ---------""")

#Procedimento que Lê um nome 
#p_nome
def p_nome():
    return(input("Nome....: "))


#Procedimento de Listagem de um registro 
#listar_dados
def listar_dados(nome, celular, email):
    print("""Nome: %s
             Celular: %s 
             Email: %s""" % (nome, celular, email))
    print("----------------------------------------")
    

#Procedimento de Listagem de todos os registros da matriz 
#listar()
def listar(): #para mostrar a lista de contatos 
    print(" CONTATOS DA AGENDA ")
    print("----------------------------------------")

    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    
    print(" FIM DA AGENDA ")


#Função que pesquisa um contato pelo nome 
#pesquisa(nome): int
def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda): #percorre a matriz 
        if e[0].lower() == name: #procura o nome 
            return d #retorna o nome encontrado 
        return None #caso não encontre 

#Exibe o registro ou mensagem de insucesso 
#pesquisar()
def pesquisar():
    #pesquisa o nome 
    p = pesquisa(p_nome()) #entrada de dados 
    if p != None:
        print("Registro encontrado! ")
        #atualiza as var se encontrou 
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        #mostra o registro 

        listar_dados(nome, celular, email)
    else:
        #exibe a mensagem de insucesso 
        print(" NOME NÃO ENCONTRADO!! ")

#Apaga um contato 
#apagar()
def apagar():
    global agenda 
    nome = p_nome()
    #retorna o índice ou vazio 
    p = pesquisa(nome)
    if p != None:
        del agenda[p] #exclui
        print(" REGISTRO APAGADO COM SUCESSO!! ")
        
    else:
        print("Nome não encontrado. ")

#Edita um contato 
#editar()
def editar():
    p = pesquisa(p_nome()) #entrada de dados 

    if p != None:
        nome = agenda[p][0]
        print("Nome....: ", nome)
        celular = input("Celular....: ")
        email = input("E-mail....: ")
        agenda[p] = [nome, celular, email] #armazenando os dados 

        print("REGISTRO EDITADO COM SUCESSO!!")

    else:
        print("Nome não encontrado. ")

#Validação se um item digitado foi válido
#validar(pergunta, inicia, fim)
def validar(pergunta, inicia, fim): #validar números inteiros 
    while True: #criando um loop infinito 
        try:  #criando acordo ou condição
            valor = int(input(pergunta))
            if inicia <= valor <= fim: #determinando uma condição 
                return (valor)
            else:
                return(0)
        except ValueError: #caso for falsa
            print("Valor inválido, favor digitar entre %d e %d " % (inicio, fim))

#retorna o item do menu ou 0 para inválido
#menu(pergunta, inicia, fim)
def menu(): #exibe o menu de opções 
    print( """
          1 - Adicionar novo contato 
          2 - Editar um contato 
          3 - Pesquisar contato 
          4 - Lista de contatos 
          5 - Apagar um contato 
          6 - Sair 
          """)
    return validar("Escolha uma opção: ", 1, 6)

#PROGRAMA PRINCIPAL 

while True: #loop infinito 
    opcao = menu()
    if opcao == 0:
        print("Opção inválida!")
    elif opcao == 6:
        print(" Obrigado por utilizar a nossa agenda !!!! ")
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()