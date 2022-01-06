import pyrebase


texto1 = 'PYREBASE, CONEXIÓN PYTHON GOOGLE FIREBASE'

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

config = {
  "apiKey": "TuApiKeyFirebase",
  "authDomain": "xxxxxx",
  "databaseURL": "https://xxxxxx.firebaseio.com",
  "storageBucket": "xxxxxx.appspot.com",
  "serviceAccount": "/Path/xxxxxx-xxxxxx-firebase-adminsdk-xxxx-xxxxxx.json" // DEBES TENER EL ARCHIVO .JSON DESCARGADO

}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
print(db.get())

auth = firebase.auth()

user = auth.sign_in_with_email_and_password("tuCorreo@gmail.com", "tuPass")
