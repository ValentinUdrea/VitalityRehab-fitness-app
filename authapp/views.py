from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"index.html")
#We will not call the function here, we will call it in the urls.py of authapp


