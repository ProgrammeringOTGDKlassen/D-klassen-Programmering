import Rumgeo as b

print('_____________________')
print('Opgave 1 fra 20090529')
print('_____________________')

print('Jeg starter med at definere mine forskellige punkter som en vector da det gør det samme.')
A = b.Vector(4,0,0)
B = b.Vector(3,5,0)
C = b.Vector(0,5,0)
D = b.Vector(0,0,0)

print('Jeg laver nu forbindende vektorer mellem de forskellige punkter')
BA = b.Vector.god_forbindende_vector(B, A)
AD = b.Vector.god_forbindende_vector(A,D)
DC = b.Vector.god_forbindende_vector(D,C)
BC = b.Vector.god_forbindende_vector(B,C)

print('Jeg regner nu arealet for en trapez, da firkanten er en trapez')
Areal = 0.5 * DC.length() * (AD.length() + BC.length())

print('Arealet af firkanten ABCD er {}'.format(Areal))

print('Jeg regner nu vinklen mellem vector BC og BA')
Vinkel = BC.vec2_vinkel(BA)

print('Vinklen mellem siden AB og siden BC er {}'.format(Vinkel))

