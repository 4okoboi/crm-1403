import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBbSIbGpsZnDSOTdLuYIDClPmdxb4vcix4",
                  'authDomain': "prod-api-1403.firebaseapp.com",
                  'databaseURL': "https://prod-api-1403-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "prod-api-1403",
                  'storageBucket': "prod-api-1403.appspot.com",
                  'messagingSenderId': "71822615601",
                  'appId': "1:71822615601:web:98d92417222c77c2512110",
                  'measurementId': "G-S4LK2EX7YY"}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

# print(database.child('countries').push('US'))

