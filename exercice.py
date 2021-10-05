#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


#Générez la liste des maximums d'une liste de listes de nombres. On veut donc le maximum de chacune des listes.
def get_maximums(numbers):
	a = [[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]

	i = 0
	liste_max = []

	while i <= len(a) - 1:
		liste_max.append(max(a[i]))
		i += 1

	return liste_max


# doit retourner un int
def join_integers(numbers):
	b = []
	i = 0

	while i <= len(numbers) - 1:
		b.append(str(numbers[i]))
		i += 1

	resultat_final = (int(''.join(b)))
	return resultat_final

#trouver tous les nombres premiers inférieurs à un certain entier naturel donné N
def generate_prime_numbers(limit):



	return [0]

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [""]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

	premiers = []
	nombres = []
	# ici, faire en sorte de faire une liste de valeurs multiple de 2 jusqu'à limit

	i = 0

	for i in range(0, 17, 2):
		nombres.append(i)

	print(nombres)

