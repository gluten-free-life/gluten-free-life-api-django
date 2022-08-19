from django.shortcuts import render

def predict(request):
    return render(request, "blog/predict.html")

# Create your views here.
