# -*- coding: utf-8 -*-

sequence = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
# Search word in a list and return indice of first of them
def search_word(element, liste):
    counter = 0
    for word in liste:
        if word == element:
            counter += 1
            if(counter == 1):
                print(liste.index(element))

# search_word(8, sequence)

# Search word in a list and return indice of each of them
def search_word_indice(element, liste):
    pos = -1
    for i in range(len(liste)):
        if liste[i] == element:
            pos = i
            print(pos)

# search_word_indice(8, sequence)
