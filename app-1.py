# -*- coding: utf-8 -*-

sequence = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
def search_word(word, liste):
    indice_counter = 0
    # if word in liste:
    #     print(word," exist dans ", liste)
    for word in liste:
        print(liste.index(word))



search_word('hakan', ['serkan', 'hakan', 'nimet'])
search_word('hakan', 'serkanhakannimet')
search_word(7, sequence)
