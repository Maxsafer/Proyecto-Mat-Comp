import re

# Let the user decide the file to use
print("What file do you want to use?")
print("1. test1.txt")
print("2. test2.txt")
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

    table[second_split[0]] = {}
    table[second_split[0]][second_split[1]] = first_split[1]

#validate(table, input, final, state[arreglo con el origen])

#def validate(table, input, final, state[arreglo con el origen])
  #for x
  #busqueda en profundida para los caminos posibles

  #returns en true y false del string

  #validate(table, input, fin_states, init_state)

def validate(table, init_state, fin_states, string):
    pass
    #for x in table:

print(table)
print(table["0"]["lambda"][1])
print(len(table["0"]["lambda"]))
#print("-------------------------------------------------------------------------")
#print("Enter the string")
#string = input()
#print(string)
#print("------------------------------------------------------------------------")