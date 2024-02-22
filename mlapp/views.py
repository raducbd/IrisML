from django.shortcuts import render,redirect
from joblib import load

# loading the ML model
model = load('./SavedModels/model.joblib')

class_labels = {
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
}
# Create your views here.
def Home(request):
    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == "Predict":
            Sepal_length = request.POST.get('sepal_length')
            Sepal_width = request.POST.get('sepal_width')
            Petal_length = request.POST.get('petal_length')
            Petal_width = request.POST.get('petal_width')
            Result = None
            predictions = model.predict([[Sepal_length,Sepal_width,Petal_length,Petal_width]])
            prediction = class_labels.get(predictions[0])
            return render(request,'index.html',{'prediction':prediction})
    else:

        return render(request,'index.html')