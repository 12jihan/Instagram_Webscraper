import pyrebase

config = {
    "apiKey": "apiKey",
    "authDomain": "insta-data-3834d.firebaseapp.com",
    "databaseURL": "https://instaAcct.firebaseio.com",
    "storageBucket": "insta-data-3834d.appspot.com",
    "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initializa_app(config)