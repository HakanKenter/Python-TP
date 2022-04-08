# -*- coding: utf-8 -*-

# __________________________________________________________________PARTIE 1______________________________________________________________________________

# 1 - Première exercice

populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

relation_key = {'relation': []}
for population in populations:
    population.update(relation_key)
    mon_array = []
    for relation_tuple in relationships:
        if population["id"] in relation_tuple:
            mon_array.append(relation_tuple)
    population.update({'relation': mon_array})
    # print(population)
print(populations)


# 2 - Deuxième exercice




