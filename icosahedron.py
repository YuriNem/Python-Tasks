from math import sqrt

edge = float(input('Input icosahedron edge length: '))
print('\n')

if edge <= 0:
    print('Uncorrect length')
else:
    volume = 5 * (edge ** 3) * (3 + sqrt(5)) / 12
    surfaceArea = 5 * (edge ** 3) * sqrt(3)
    radiusInscribedSphere = edge * sqrt(3) * (3 + sqrt(5)) / 12
    radiusDescribedSphere = edge * sqrt(2 * (5 + sqrt(5))) / 4

    print('Volume of icosahedron: {:.5g}'.format(volume))
    print('Surface area of icosahedron: {:.5g}'.format(surfaceArea))
    print('Radius inscribed sphere of icosahedron: {:.5g}'.format(radiusInscribedSphere))
    print('Radius described sphere of icosahedron: {:.5g}'.format(radiusDescribedSphere))
