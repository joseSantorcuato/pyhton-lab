

import time
texto1 = 'CICLO FOR'
texto2 =  'Python en español'
texto3 = 'José Luis Santorcuato Tapia'
espacio = '   '
an = '2021'



print(espacio)
print(texto1)
print(texto2)
print(texto3)
print(an)
print(espacio)

print([x + 5 for x in [2, 3, 4]])

print('Voy a contar números de 0 a 10')

for numero in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    time.sleep(1)
    print(numero)

print('Terminé de contar!')

