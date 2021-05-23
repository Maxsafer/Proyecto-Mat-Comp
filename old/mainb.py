import re

# Let the user decide the file to use
print("What file do you want to use? --1 for test1.txt-- --2 for test2.txt--")
opcion = int(input())

if opcion == 1:
    f = open("test1.txt", "r")
elif opcion == 2:
    f = open("test2.txt", "r")

# Obtain general data of the file
data = f.readlines()
file_length = len(data)

states = data[0].rstrip().split(',')  # states
alphabet = data[1].rstrip().split(',')  # alphabet
init_state = data[2].rstrip().split(',')  # init_state
init_state[0] = init_state[0].replace('q','')
fin_states = data[3].rstrip().split(',')  # fin_states

table = {}
counter = 0

for x in range(4, file_length):
    line = data[x].rstrip()
    first_split = re.split("=>", line)
    second_split = re.split(",", first_split[0])

    first_split[0] = first_split[0].replace('q','')
    first_split[1] = first_split[1].replace('q','')
    second_split[0] = second_split[0].replace('q','')
    first_split[0] = first_split[0].replace(',','')
    first_split[1] = first_split[1].replace(',','')
    second_split[0] = second_split[0].replace(',','')

    table[second_split[0]] = {}
    table[second_split[0]][second_split[1]] = first_split[1]

for i in table:
    print(i, table[i])
print('------------------------------------------------------')
''''
for i in table:
    print(i)
    for j in table[i]:
        print(j)
'''
print('-------------------------------------------------------')


print("What string do you want to use:")
string = input()

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node][list(graph[node].keys())[0]]:
            dfs(visited, graph, neighbour)

def search(state, string_char, table):
    print('state: ', state, 'char: ', string_char)
    
    #print(list(table[state].keys())[0]) acceder al value del key
    dfs(visited, table, state)
    if ("lambda" == list(table[state].keys())[0]):
      
      dfs(visited, table, state)
      
      #print(len(table["0"]["lambda"]))
      print(table[state]["lambda"][0])
      print("yey!")

      #pasosen string = false

    if (string_char == list(table[state].keys())[0]):
      print("yey!")

      #pasosen string = true
      #else bool false

    if (len(string_char) == 0):
        print("no idea")

def check(table, string, state):
    for element in range(0, len(string)): #
        #if pasosen string == false -> le restamos a element 1
        search(list(table.keys())[int(state)], string[element], table)

check(table, string, init_state[0])

#def validate(table, input, final, state[arreglo con el origen])
  #for x
  #busqueda en profundida para los caminos posibles

  #returns en true y false del string

  #validate(table, input, fin_states, init_state)
