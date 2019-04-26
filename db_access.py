import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate('../keys/ServiceAccountKey.json')
# default_app = firebase_admin.initialize_app(cred)

# db = firestore.client()

# # Reference to instaAccts collection and data with in it
# coll_ref = db.collection(u'InstaAccts')
# doc_ref = coll_ref.document()

# # Add data to the database (firestore)
# doc_ref.set({
#     u'username': u'DemiG.od',
#     u'followers': 1012,
#     u'following': 627,
#     u'posts': 0
# })

# # Read data from the database (firestore)
# docs = coll_ref.stream()

# print(docs)

# for doc in docs:
#     print(str(doc.to_dict()))

# sprint(default_app.name)

class Firebase_DB_Access:
   
    cred = credentials.Certificate('./keys/ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    coll_ref = db.collection(u'instaAccts')
    doc_ref = coll_ref.document()

    # def __init__(self, a, b, c):

    def postData(self, username):
        self.username = username

        doc_ref.set({
            u'username': self.username
        })
    
    def readData(self):
        docs = coll_ref.stream()
        print(self.docs)

fdb = Firebase_DB_Access()
fdb.postData('demig.od')