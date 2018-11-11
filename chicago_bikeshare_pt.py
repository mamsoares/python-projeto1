# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
#with open("chicago-teste.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.
#['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
#      0            1            2                 3              4               5          6         7         

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("\nAperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#Essa amostra ainda possui o cabcelho na linha 0 por isso começa a partir da linha 1 até 21
for x in range(1,21):
    print("\nLinha {}: {}".format(x,data_list[x]))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# PRIMEIRA VERSAO - ANTES DA REVISAO
#for x in range(0,20):
#    gender = data_list[x]
#    print("\nGênero {}: {}".format(x+1,gender[6])) #Soma 1 para mostrar o sequencial correto já que removemos o cabecalho

#DEPOIS DA REVISAO
for i, vlinha in enumerate(data_list[:20], start=1):
    print("Linha: {}\tGênero: {}".format(i, vlinha[6]))
    #print(f"Linha: {i}\tGênero: {vlinha[-2]}\tGênero: {vlinha}")


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("\nAperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    """
    Funcao cria uma lista baseada nas colunas da lista recebida
    Argumentos:
      data: Lista origem.
      index: numero da coluna.
    Retorno:
       A lista da coluna recebida
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for var_linha in data:
        column_list.append(var_linha[index])    

    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
#assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for linha in data_list:
    gender = linha[-2]
    male += gender == 'Male'
    female += gender == 'Female'

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
#assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Funcao para contagem da coluna genero
    Argumentos:
      data: Lista origem
    Retorno:
       A lista dos generos
    """       
    male = 0
    female = 0
    for x in data_list:
        gender = x[-2]
        male += gender == 'Male'
        female += gender == 'Female'

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
#assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Funcao para identificar o genero mais popular ou se são iguais
    Argumentos:
      data: Lista origem
    Retorno:
       Uma resposta string
    """ 
    answer = ""
    vmale, vfemale = count_gender(data_list)

    if vmale > vfemale:
        answer = 'Male'
    elif vmale < vfemale:
        answer = 'Female'
    else:
        answer = 'Equal'

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Dependent", "Subscriber"]

#PRIMEIRA VERSAO - ANTES DA REVISAO
#quantity = [user_types_list.count("Customer"), user_types_list.count("Dependent"), user_types_list.count("Subscriber") ]
#print("Customer:{}\nDependent:{}\nSubscriber:{}".format(quantity[0], quantity[1], quantity[2]))

#DEPOIS DA REVISAO
def count_user_types(user_data_list):
    """
    Funcao para contagem do tipo de usuario pre-definidos na lista
    Argumentos
      data: lista de usuarios
    Retorno:
       A lista contendo os tipos de usuarios pre-definidos e 
       array com os totais de cada tipo de usuario para o grafico
    """
    qt_customer = 0
    qt_dependent = 0
    qt_subscriber = 0

    for user in user_data_list:
        qt_customer += user == 'Customer'
        qt_dependent += user == 'Dependent'
        qt_subscriber += user == 'Subscriber'

    colunas = [qt_customer, qt_dependent, qt_subscriber]

    return [qt_customer, qt_dependent, qt_subscriber, colunas]

customer, dependent, subscriber, quantity = count_user_types(user_types_list)


print("Customer:{}\nDependent:{}\nSubscriber:{}".format(customer, dependent, subscriber))

input("\nAperte Enter para continuar...")

y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de usuário')
plt.show(block=True)


input("\nAperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list): ", male + female == len(data_list))
answer = "Porque existem {} registro(s) sem o preenchimento correto do gênero.".format(len(data_list) - (male + female))
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você NÃO deve usar funções prontas para isso, como max() e min().
lista_tempo_duracao = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# Iniciando as variáveis
min_trip = float(lista_tempo_duracao[0])
max_trip = float(lista_tempo_duracao[0])
somatorio_trip = 0

# Fazendo os elementos da lista virarem float
lista_tempo_duracao = list(map(float,lista_tempo_duracao))

# Buscando max, min e realizando a soma
for trip in lista_tempo_duracao:
    somatorio_trip += trip

# Ordenando para achar o mediana, também poderia ser usada para achar o min e max, pegando o primeiro e último elemento.
lista_tempo_duracao_ordenada = sorted(lista_tempo_duracao)
tamanho_lista = len(lista_tempo_duracao)

# Arredondando a saída
max_trip = round(lista_tempo_duracao_ordenada[len(lista_tempo_duracao_ordenada) - 1])
min_trip = round(lista_tempo_duracao_ordenada[0])
mean_trip = round(somatorio_trip/tamanho_lista)

#Para o cálculo da mediana você primeiro precisa verificar o tamanho da lista, 
#caso for IMPAR basta pegar o valor do meio ( foi o que você fez), 
#caso for de tamanho PAR você precisa tirar a média do dois valores do meio.
if tamanho_lista % 2 == 1:
    median_trip = int(lista_tempo_duracao_ordenada[tamanho_lista//2])
else:
    median_trip = int((lista_tempo_duracao_ordenada[tamanho_lista//2 -1]+lista_tempo_duracao_ordenada[tamanho_lista//2]) / 2)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
  Argumentos:
      param1: O primeiro parâmetro.
      param2: O segundo parâmetro.
  Retorna:
      Uma lista de valores x.
"""

input("\nAperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("\nVocê vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
        Função para contar tipos de usuários, sem definir os tipos
        para que nós possamos usar essa função com outra categoria de dados.
        Argumentos:
            column_list: A lista de itens (list).
        Retorna:
            item_types - os tipos diferentes de itens na lista.
            count_items - quantidade de cada tipo de itens na lista.
    """
    items_set = set(column_list)
    print(items_set)

    #INICIALIZAR LISTAS
    item_types = []
    count_items = []
    
    for item in items_set:
        item_types.append(item)
        count_items.append(column_list.count(item))

    return [item_types, count_items]

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -3)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("\nTipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    input("\nAperte Enter para visualizar o grafico...")

    y_pos = list(range(len(types)))
    plt.bar(y_pos, counts)
    plt.ylabel('Quantidade')
    plt.xlabel('Tipos de usuários')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Tipo de usuário')
    plt.show(block=True)



    # ------------ CÓDIGO UTILIZANDO A COLUNA GENERO ------------
    column_list = column_to_list(data_list, 6)
    types, counts = count_items(column_list)
    print("\nTAREFA 13: Imprimindo resultados para count_items()")
    print("\nTipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 13: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    input("\nAperte Enter para visualizar o grafico...")

    y_pos = list(range(len(types)))
    plt.bar(y_pos, counts)
    plt.ylabel('Quantidade')
    plt.xlabel('Gêneros')
    plt.xticks(y_pos, types)
    plt.title('Quantidade por Gênero')
    plt.show(block=True)