texto1 = 'OPERADORES LÓGICOS'

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

variableA = 5

variableB = 8

if variableA > 3 and variableB > 5:
       print("Se cumplen ambas condiciones")
if variableA > 4 or variableB <= 8:
       print("VariableA es mayor a 4 y variableB es igual a 8")
else:
       print("Mayor a 6")
while variableA > 0:
       print('variableA es {}' .format(variableA))
       variableA -=1
print(espacio)
for x in ['a', 'b', 'c', 'd']:
       print(x)
print(espacio)
for i in range(10):
       print(i)
print(espacio)
print([j + 5 for j in [2, 3, 4]])