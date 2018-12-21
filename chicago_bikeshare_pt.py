# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
data_list=[]
with open("chicago.csv", "r") as file_read:
    first_line = True
    for line in file_read:
      if first_line:
        keys = "".join(line.split('\n')).split(',')
        data_list.append(keys)
        first_line = False
      else:
        values="".join(line.split("\n")).split(',')
        data_list.append(values)
    
    


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

raw_input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
for i, linha in enumerate(data_list[:20]):

  if(i == 0):
    line = 'num |\t{:<20}\t|\t{:<20}\t|\t{:<8}\t|\t{:<50}\t|\t{:<50}\t|\t{:<10}\t|\t{:<8}\t|\t{}'.format(data_list[0][0],data_list[0][1],data_list[0][2],data_list[0][3],data_list[0][4],data_list[0][5],data_list[0][6],data_list[0][7])
  else:
    line = '{:<4}|\t{:<20}\t|\t{:<20}\t|\t{:<8}\t|\t{:<50}\t|\t{:<50}\t|\t{:<10}\t|\t{:<8}\t|\t{}'.format(i,data_list[i][0],data_list[i][1],data_list[i][2],data_list[i][3],data_list[i][4],data_list[i][5],data_list[i][6],data_list[i][7])
  print(line)

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

raw_input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(21):
  if(i == 0):
    line = 'num |\t{:<20}\t'.format(data_list[0][6])
  else:
    line = '{:<4}|\t{:<20}\t'.format(i,data_list[i][6])
  print(line)

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

raw_input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Essa função cria uma lista com todos os valores de uma determinada coluna
    Argumentos:
          data: A lista original contendo todas as tuplas e colunas.
        index: Índice da coluna que vai ser extraída da lista original.
    Retorna:
        Uma lista com todos os valores(exceto o header) da coluna 'index' da lista 'data'
    """
    column_list = []
    for line in data:
      if(line[index] != data[0][index]):
        column_list.append(line[index])
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = column_to_list(data_list,-2).count('Male')
female = column_to_list(data_list, -2).count('Female')


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: {}\nFemininos: {}".format(male, female))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Essa função cria uma lista com a quantidade de ocorrências de 'Male' e 'Female'
    Argumentos:
      data_list: A lista inteira contendo todas as tuplas da coluna 'Gender'.
    Retorna:
      Uma lista com a quantidade de ocorrências de Male e Female respectivamente
    """
    male = column_to_list(data_list,-2).count('Male')
    female = column_to_list(data_list, -2).count('Female')
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Essa função verifica qual foi o sexo mais recorrente nos aluguéis de bicicleta
    Argumentos:
      data_list: A lista original contendo a coluna 'Gender' completa
    Retorna:
      Uma string com o sexo que tem mais registros dentro da data_list
    """
    answer = ""
    male, female = count_gender(data_list)
    if male == female:
      answer = 'Equal'
    elif male > female:
      answer = 'Male'
    else:
      answer = 'Female'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: {}".format(most_popular_gender(data_list)))

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
plt.ylabel(u'Quantidade')
plt.xlabel(u'Gênero')
plt.xticks(y_pos, types)
plt.title(u'Quantidade por Gênero')
plt.show(block=True)

raw_input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, -3)
types = list(set(user_types_list))
quantity = [user_types_list.count(t) for t in types]
y_pos = list(range(len(types)))
plt.bar (y_pos, quantity)
plt.ylabel(u"Quantidade")
plt.xlabel(u"Tipo de Usuário")
plt.xticks(y_pos, types)
plt.title(u"Quantidade por Tipo de Usuário")
plt.show(block=True)

raw_input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existem alguns registros que não possuem informação no campo 'Gender'."
print("resposta: {}".format(answer))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

def getMediana(lista):
  """
  Essa função descobre o valor mediano da lista
  Argumentos:
    lista: A lista original contendo todos os valores
  Retorna:
    um float com o valor de mediana
  """
  middle = len(trip_duration_list)/2
  if (len(trip_duration_list)%2) != 0:
    middle = int(round(middle))
    return (trip_duration_list[middle]+ trip_duration_list[middle-1])/2
  else:
    return (trip_duration_list[int(middle)])

trip_duration_list = sorted(list(map(int , column_to_list(data_list, 2))))
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = float(sum(trip_duration_list))/float(len(trip_duration_list))
median_trip = getMediana(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: {}\nMax: {}\nMédia: {}\nMediana: {}".format(min_trip, max_trip, mean_trip, median_trip))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list,4))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

raw_input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      # """
      # Função de exemplo com anotações.
      # Argumentos:
      #     param1: O primeiro parâmetro.
      #     param2: O segundo parâmetro.
      # Retorna:
      #     Uma lista de valores x.

      # """

raw_input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    """
    Realiza uma contagem de indices e quantidades
    Argumentos:
      column_list: A lista que deverá ser analisada
    Retorna:
      um array com dois arrays as chaves diferentes e a quantidade de cada chave
    """
    item_types = list(set(column_list))
    count_items = [column_list.count(t) for t in item_types]
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
