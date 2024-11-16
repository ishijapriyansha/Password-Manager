from django.shortcuts import render
import pymongo
from django.conf import settings
from datetime import datetime

# Establish MongoDB connection
client = pymongo.MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
collection = db[settings.MONGO_COLLECTION_NAME]

def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        password = request.POST['password']

        # Insert the password data into MongoDB
        collection.insert_one({
            'title': title,
            'password': password,
            'created_at': datetime.now()  # Add timestamp
        })

    # Fetch all stored passwords from MongoDB
    passwords = collection.find()

    return render(request, 'passwords/home.html', {'passwords': passwords})
