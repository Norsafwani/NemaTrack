from django.http import HttpResponse
from django.shortcuts import render, redirect
from trackApp.models import AuthUser

# Create your views here.


# def home(request):
#     return render(request, 'login.html') 

def home(request):
    if request.session._session:
        user_id = request.session['id']
        user = AuthUser.objects.filter(id=user_id)
        return render(request, 'home.html', {'user':user})
    return render(request, 'login.html') 

# def home(request):
#     if request.session._session:
#         user_id = request.session['id']
#         user = AuthUser.objects.filter(id=user_id)
#         return render(request, 'home.html', {'user':user})
#     return redirect('/login')