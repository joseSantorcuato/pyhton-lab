from decimal import Decimal as dc
texto1 = 'MATEMÁTICAS DECIMALES'

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

# EJECUCIÓN

print(dc(3.14))
print(dc('3.14\n'))

print(dc(0.1) * dc(0.2) * dc(0.3))
print(dc('0.1') * dc('0.2') * dc('0.3'))
print(dc('1.4').as_integer_ratio())


