import os
import sys

###################################################################################################
#                                                                                                 #
#                                       Question 01                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################


def Question01(data, number):
    count = data.count(number)
    if count == 0:
       print("The integer does not repeat")

    else:
        print(count)


###################################################################################################
#                                                                                                 #
#                                       Question 02                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################


def Question02(data):
    Min = min(data)
    Max = max(data)
    print(Min)
    print(Max)


###################################################################################################
#                                                                                                 #
#                                       Question 03                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################


def Question03(myDict):
    myDict = {}
    endWrite = '0'
    key = input('Type in the key: ')
    value = input('Type in the value:')
    while key != '0':
        myDict[key] = value
        key = input('Type in the key: ')
        value = input('Type in the value:')

    print(myDict)

###################################################################################################
#                                                                                                 #
#                                       Question 04                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################

def Question04(TupleExample):
    key = input('Type in the index: ')
    index = int(key)
    if index <= len(TupleExample):
        print(TupleExample[index])
    else:
        print("Error")



###################################################################################################
#                                                                                                 #
#                                       Question 05                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################

def Question05(TupleContents):
    index = len(TupleContents)

    for var in range (len(TupleContents)):
        print("Estimado " + TupleContents[var] + " vote por mí")







###################################################################################################
#                                                                                                 #
#                                       Question 06                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################

def Question06(ListReverse):
    NewList = ListReverse[::-1]
    print(ListReverse)
    print (NewList)




###################################################################################################
#                                                                                                 #
#                                       Question 07                                               #
#                                                                                                 #
#                                                                                                 #
###################################################################################################


def Question07(tupla, tupla2):
    if tupla[0] in tupla2 or tupla[1] in tupla2:
        print("Si encajan")
    else:
        print("No se encajan")




data = (1, 2, 3, 4, 1, 5, 7, 1, 4, 4)

data2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

number = 1

myDict = {}

TupleSearch = ("One", "Two", "Three", "Four", "Five")

TupleNames = ("John", "Frank", "Andrew")

Tupla01 = (1,3)
Tupla02 = (3,6)

UserInput = input("Type in the desired Question: \nPress 0 to quit \n")

QuestionNumber = int(UserInput)

while QuestionNumber != 0:

    if QuestionNumber == 1:
        print("Question One: \n")
        Question01(data, number)
        break

    elif QuestionNumber == 2:
        print("Question Two: \n")
        Question02(data2)
        break

    elif QuestionNumber == 3:
        print("Question Three: \n")
        Question03(myDict)
        break

    elif QuestionNumber == 4:
        print("Question Four: \n")
        Question04(TupleSearch)
        break

    elif QuestionNumber == 5:
        print("Question Five: \n")
        Question05(TupleNames)
        break

    elif QuestionNumber == 6:
        print("Question Six: \n")
        Question06(data)
        break

    elif QuestionNumber == 7:
        print("Question Seven: \n")
        Question07(Tupla01, Tupla02)
        break

    else:
        print("Please enter a valid question number.")


#Question01(data, number)

#Question02(data)

#Question03(myDict)

#Question04(TupleSearch)

#Question05(TupleNames)

#Question06(data)

#Question07(Tupla01, Tupla02)
