#Немушкин Юрий ИУ7-14Б

import math

edge = int(input("Input icosahedron edge's length: "))

volume = (5 * (edge ** 3) * (3 + math.sqrt(5))) / (12)
surfaceArea = 5 * (edge ** 3) * math.sqrt(3)
radiusInscribedSphere = (edge * math.sqrt(3) * (3 + math.sqrt(5))) / (12)
radiusDescribedSphere = (edge * math.sqrt(2 * (5 + math.sqrt(5)))) / (4)

print('Volume of icosahedron: {:.2f}'.format(volume))
print('Surface area of icosahedron: {:.2f}'.format(surfaceArea))
print('Radius inscribed sphere of icosahedron: {:.2f}'.format(volume))
print('Radius described sphere of icosahedron: {:.2f}'.format(volume))
