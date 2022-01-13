texto1 = 'CONDICIONALES - LOOPS'

texto2 = 'Python en español'
texto3 = 'José Luis Santorcuato Tapia'
espacio = '   '
an = '2021'

print(espacio)
print(texto1)
print(texto2)
print(texto3)
print(an)
print(espacio)

# EJECUCIÓN

variable = 5
if variable < 3:
       print("Menor que 3")
elif variable < 6:
       print("Menor a 6")
else:
       print("Mayor a 6")
while variable > 0:
       print('variable es {}' .format(variable))
       variable -=1
print(espacio)
for x in ['a', 'b', 'c', 'd']:
       print(x)
print(espacio)
for i in range(10):
       print(i)
print(espacio)
print([j + 5 for j in [2, 3, 4]])