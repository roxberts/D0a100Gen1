import os

# #structured programming
#
# animal = input('Write the name of the animal: ')
#
# if animal == 'gato':
#     animallegs = 4
#     print('This animal has '+str(animallegs)+' legs.')
# elif animal == 'perro':
#     animallegs = 4
#     print('This animal has '+str(animallegs)+' legs.')
# elif animal == 'spider':
#     animallegs = 8
#     print('This animal has '+str(animallegs)+' legs.')
# else:
#    print("I don't know that animal")

#modular programing

# animals = {'gato':4,'perro':4,'spider':8}
#
# def getName():
#     animal = input('Write the name of the animal: ')
#     return animal
#
# def setAnimal(animal):
#     if animal not in animals:
#         print("I don't know that animal")
#         animallegs = 0
#     else:
#         animallegs = animals[animal]
#     return animallegs
#
# def describeAnimal(animallegs):
#     print('This animal has '+str(animallegs)+' legs. ' )
#
# animal = getName()
# animallegs  = setAnimal(animal)
# if animallegs > 0:
#     describeAnimal(animallegs)
#
# #Object Oriented Programming
#
# class Animal(object):
#
#     def __init__(self):
#         print('Instanciating animal class')
#         self.name = input('Write the name of the animal: ')
#         self.animallegs = 0
#
#     def setAnimal(self):
#         animals = {'gato':4,'perro':4,'spider':8}
#         animal = self.name
#         if animal not in animals:
#     	       print("I don't know that animal")
#         else:
#             self.animallegs = animals[animal]
#
#     def describeAnimal(self):
#         print('This animal has '+str(self.animallegs)+' legs. ')
#
# animal = Animal()
# animal.setAnimal()
# if animal.animallegs > 0:
#     animal.describeAnimal()
