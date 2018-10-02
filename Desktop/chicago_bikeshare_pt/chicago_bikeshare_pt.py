# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
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

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
[print(item) for item in data_list[0:20]]
# Esta função gera uma nova lista, ignorando o índice 0
data_list = data_list[1:]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# Esta função imprime a coluna de indice 5 para cada item nos indices de 0 até 20 no dataset

[print(item[6]) for item in data_list[0:20]]

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

#Esta funcção recebe como parametro o dataset completo e o indice cujo vai retornar em forma de lista
def column_to_list(data, index):
    column_list = []
    [column_list.append(data[index]) for data in data]
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

# Aqui uma lista é gerada com indice de colinuna 6 para cada linha do dataset, após isto a função count conta quantos de cata tipo existem
male = list(row[6] for row in data_list).count('Male')
female = list(row[6] for row in data_list).count('Female')

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


# Aqui uma lista é gerada com indice de colinuna 6 para cada linha do dataset, após isto a função count conta quantos de cata tipo existem
# depois os valores subsequentes retornam em um array
def count_gender(data_list):
    male = list(row[6] for row in data_list).count('Male')
    female = list(row[6] for row in data_list).count('Female')
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

# Esta funcao compara os tamanhos dos arrays e retorna o valor referente ao tipo de dados contido neste.
def most_popular_gender(data_list):
    gender_values = count_gender(data_list)
    return 'Male' if gender_values[0] > gender_values[1] else 'Female' if gender_values[0] < gender_values[1] else 'Equal'
    
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

# Esta funcao recebe como parametro o dataset completo, conta quantos usuariso de cada tipo tem na coluna de indice 5 de cada linha do dataset
def count_user_type(data_list):
    customer = list(row[5] for row in data_list).count('Customer')
    subscriber = list(row[5] for row in data_list).count('Subscriber')
    return [customer, subscriber]

print("\nTAREFA 7: Verifique o gráfico!")
gender_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Algumas linhas tem esse campo em branco."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

#Esta funcao recebe uma lista, pega o primeiro indice e armazena o valor do mesmo em uma variavel, e compara os demais, substituindo o valor da variavel caso o valor 
# do indice corrente no laço seja maior
def get_max(trip_list):
    maximum = int(trip_list[0])
    for item in trip_list:
        if int(item) > maximum:
            maximum = int(item)
    return maximum  

#Esta funcao recebe uma lista, pega o primeiro indice e armazena o valor do mesmo em uma variavel, e compara os demais, substituindo o valor da variavel caso o valor 
# do indice corrente no laço seja menor
def get_min(trip_list):
    minimum = int(trip_list[0])  
    for item in trip_list:
        if int(item) < minimum:
            minimum = int(item)   
    return minimum  

#Esta funcao recebe uma lista, realiza a ordenacao da mesma, mede o tamanho da lista e verifica se o tamanho é par ou impar
# caso seja par soma os indices nas posicoes metade + 1 e metade -1 e divide por 2. Caso seja impar retorna o resultado da divisao
# inteira do tamanho da lista + 1 dividido por 2
def get_median(trip_list):
    sorted_list = sorted(trip_list, key=int)
    list_len = len(sorted_list)
    if list_len % 2 == 0:
        return (sorted_list[round((list_len-1)//2)] + sorted_list[round((list_len+1)//2)]) // 2
    else:
        return sorted_list[(list_len+1)//2]
#Esta funcao recebe uma lista, e retorna o resultado da soma todos valores dividido pelo tamanho da lista
def get_mean(trip_list):
    list_len = len(trip_list)
    list_sum = 0
    for item in trip_list:
        list_sum += int(item)
    return round(list_sum / list_len)        

min_trip = get_min(trip_duration_list)
max_trip = get_max(trip_duration_list)
median_trip = get_median(list(map(int, trip_duration_list)))
mean_trip = get_mean(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

#Aqui foi utilizada a funcao set que retorna os elementos unicos de uma lista montada a partir da quarta coluna do dataset
start_stations = set((column_to_list(data_list, 3)))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.

#      
input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = set((column_to_list(data_list, 5)))
    count_items = []
    [count_items.append(1) for data in data_list]
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
