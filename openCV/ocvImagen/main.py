

texto1 = 'OPEN CV CARGAR IMAGEN'
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




import cv2

img = cv2.imread('opencv.png')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()