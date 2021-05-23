import re

# Let the user decide the name of the file to use
print("Type the name and the extension of the file to use: ")
use_file = input()

f = open(use_file, "r")

# Obtain general data of the file
data = f.readlines()
file_length = len(data)

states = data[0].rstrip().split(",")
alphabet = data[1].rstrip().split(",")
init_state = data[2].rstrip().split(",")
fin_state = data[3].rstrip().split(",")

table = {}

# Table dictionary is filled with each line of the transition table
# adding a new key for each state
for x in range(4, file_length):
    line = data[x].rstrip()
    first_split = re.split("=>", line)
    tr = re.split(",", first_split[1])
    second_split = re.split(",", first_split[0])

    # If state exists in dictionary add the other possible transition
    if second_split[0] in table:
        table[second_split[0]][second_split[1]] = tr
    # Else create a new state
    else:
        table[second_split[0]] = {}
        table[second_split[0]][second_split[1]] = tr


def printTable():
    print("-----------------------------")
    print("Transition table:")
    print("-----------------------------")
    for i in table:
        print(i, table[i])
    print("-----------------------------")


print("Input the string you want to process")
theString = input()

# Three methods should be present
# Lambda closure. Receive a set of state, return set of states
# Transition function. Receive state and char. Return states
# Extended transition function. Receive state and string, return set of states
# lambdaC(trF U etrF)


def transitionFunc(state, char):
    # return table[state][char]
    if char in table[state]:
        return table[state][char]
    else:
        return state


def lambdaC(statesC):  # lambdaC(q0, q1, q5)
    tempState = []
    tempState.extend(statesC)
    for i in statesC:
        # if transitionFunc(i, "lambda") not in lStates:
        temp = transitionFunc(i, "lambda")
        if type(temp) == str:
            tempState.append(temp)
        else:
            tempState.extend(temp)

    set(tempState)
    return list(tempState)


def extendedTransitionFunc(state, string):
    pass


testState = ["q0"]
#otra = ["q4", "q5"]
# otra.extend(testState)
# print(otra)
# print(lambdaC(testState))
printTable()
print(lambdaC(testState))

#print(transitionFunc("q0", "lambda"))
