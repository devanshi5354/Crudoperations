from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.conf import settings


# Insert Data
def insert_data(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')  # Get emp_id from the form (it will be a string)
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        client = MongoClient(settings.MONGO_URI)
        db = client.emp
        collection = db.data

        # Prepare the document to insert
        document = {
            'emp_id': emp_id,  # emp_id remains a string
            'name': name,
            'age': age,
            'email': email
        }

        # Insert the document into MongoDB
        collection.insert_one(document)

        # After inserting, redirect to a success page or back to a list of employees
        return redirect('home')  # This should be the name of your homepage or employee listing page

    return render(request, 'insert_data.html')




def home(request):
    # Render your homepage template here
    return render(request, 'home.html')

