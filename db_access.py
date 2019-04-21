import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./other/ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

# Reference to instaAccts collection and data with in it
coll_ref = db.collection(u'instaAccts')
doc_ref = coll_ref.document()

# Add data to the database (firestore)
doc_ref.set({
    u'Username': u'6',
    u'last': u'Lovelace',
    u'born': 1818,

})

# Read data from the database (firestore)
docs = coll_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))


print(default_app.name)