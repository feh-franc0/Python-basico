# FUNÇÕES, para usar funções use a palavra 'def'
def mensagens_iniciais():
    print("Boas Vindas ao Python The Game!")
    print("REGRAS")
    print("Ao longo do jogo serão exibidas perguntas que você deve responder pelo teclado")

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

mensagens_iniciais()
print("Gostaria muito de Saber seu nome!")
# DICIONÁRIO , PERMITE O AGRUPAMENTO DE DADOS DENTRO DE UMA ÚNICA ESTRUTURA
# EXEMPLOS DE USO DO DICIONÁRIO
# personagens = {
#         "Yoda":"Mestre Jedi",
#         "Mace Windu":"Mestre Jedi",
#         "Anakin Skywalker":"Cavaleiro Jedi",
#         "R2-D2":"Dróide",
#         "Dex":"Balconista"
# }
#
# print(personagens.keys())
# for chave in personagens.keys():
#         print(chave)
#
# print("\n")
#
# print(personagens.values())
# for valores in personagens.values():
#         print(valores)
#
# print("\n")
#
# for chave, valor in personagens.items():
#         print("O personagem {} pertence à classe {}".format(chave,valor))
#
# print("\n")
#
# ira tirar o ultimo item
# personagens.popitem()
# for chave, valor in personagens.items():
#         print("O personagem {} pertence à classe {}".format(chave,valor))
#
#
# print("\n")
#
#
# ira tirar o item que tem a chave igual ao que passarmos
# personagens.pop("Anakin Skywalker")
# for chave, valor in personagens.items():
#         print("O personagem {} pertence à classe {}".format(chave,valor))
#
#
#
dados_jogador = {}
dados_jogador["nome"] = input("Digite o seu nome: ")
print("Olá, {}! É um prazer ter você jogando o nosso jogo".format(dados_jogador["nome"]))

idade_jogador = int(input("Eu gostario de saber a sua idade. Em que ano você nasceu?"))


dados_jogador["idade"] = calcular_idade(idade_jogador, 2021)

print("Pelo que pude calcular, a sua idade é {}".format(dados_jogador["idade"]))


# IF = SE , Comando de Tomada de Decisão
print("Agora que já conheço sobre você, posso te levar para um universo com muitas aventuras?")
escolha = input("SIM - quero iniciar uma aventura \nNÃO - quero ficar por aqui")

if "SIM" == escolha:
        print("Que bom que você é um aventureiro! Vamos iniciar nossa missão")
        # WHILE = ENQUANTO , ENQUANTO A CONDIÇÃO FOR VERDADEIRA O LOOPING SE REPETE
        resposta = ""
        tentativas = 0
        while resposta != "42":
            resposta = input("Qual é a resposta para a vida, o universo e tudo mais?")
            tentativas = tentativas + 1
            #break
        print("Parabéns! Douglas Adams ficaria orgulhoso de você!")
        print("Para chegar a esse resultado você utilizou {} tentativas".format(tentativas))
        print("Para cada tentativa feita, você merece um parabéns!")
        # FOR = LOOP BASEADO EM CONTADOR , É BASEADO EM CONTADOR
        # BREAK = INTERROMPA , INTERROMPE A EXECUÇÃO DO LOOPING(while, for )
        # for i in range(5):
        for i in range(tentativas):
            print("Parabéns!")

        # TUPLAS , ARMAZENA UMA SEQUÊNCIA DE DADOS QUE NÃO PODEM SER ALTERADOS
        anos_lancamento = (1977, 1980, 1983, 1999, 2002, 2015, 2017, 2019)
        star_wars = int(input("Já vi que você é meio geek! É capaz de responder em que ano algum dos filmes de star wars foi lançado?"))
        if star_wars in anos_lancamento:
            print("Parabéns, você acertou! vai ganhar um prêmio")
        else:
            print("Aparentemente você não é tão geek assim.")


        # LISTAS , ARMAZENA UMA SEQUÊNCIA DE DADOS QUE PODEM SIM SER ALTERADAS
        # PARA REMOVER VALORES USE O POP(), remove um item na lista
        print("Estou tão surpreso que você é um geek que gostaria de te dar a oportunidade de escrever e armazenar alguns comandos em python")
        print("Quando tiver digitado TODOS os comandos que conhece, digite SAIR")
        comando = ""
        lista_de_comandos = []
        while comando != "SAIR":
                comando = input("Digite um comando que você conheça em Python: ")
                lista_de_comandos.append(comando)
        print(lista_de_comandos)
else:
    if "NÃO" == escolha:
            print("Pena que você não quer se aventurar!\nGAME OVER!")
    else:
        print("Você digitou um comando inválido. Jogo Encerrado.")


# ESTRUTURA DE DADOS(TUPLA, LISTAS)
# DICIONARIO = ESTRUTURA DE DADOS BASEADA NO CONCEITO DE CHAVE E VALOR {}

