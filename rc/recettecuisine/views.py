from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recette
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.views import View
from django.db import models




# Create your views here.
def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('index')
            else:
                return redirect('Home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request,'login.html')

@login_required
def Index(request):
    data = Recette.objects.all()
    return render(request,'index.html',{'recettes' : data})
    #return render(request,'index.html')

@login_required
def Home(request):
    recipes = Recette.objects.all()[:15]
    return render(request, 'Home.html', {'recipes': recipes})

@login_required
def createRecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'createRecipe.html', {'form':form})

@login_required
def updateRecipe(request,pk):
    recette = get_object_or_404(Recette,pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recette)
        form.save()
        return redirect('index')    
    else:
        form = RecipeForm(instance=recette)
    return render(request,'updateRecipe.html', {'form':form, 'recette':recette})

'''def recipe_list(request):
    data = Recette.objects.all()
    return render(request,'index.html',{'recettes' : data})'''


@login_required
def deleteRecipe(request,pk):
    recette = Recette.objects.get(pk=pk)
    recette.delete()
    return redirect('index')

def logOut(request):
    logout(request)
    return redirect('login')


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConf = request.POST.get('passwordConf')
        if password != passwordConf:
            messages.error(request, 'Passwords do not match.')
        elif username == '' or email == '' or password == '' or passwordConf == '':
            messages.error(request, 'Enter all informations.')
        else:
            try:
                myUser = User.objects.create_user(username,email,password)
                myUser.save()
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'This username is already taken. Please choose a different username.')
    return render(request,'signup.html')

def search_recipes(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        recipes = Recette.objects.filter(
            models.Q(title__icontains=keyword) |
            models.Q(ingredients__icontains=keyword) |
            models.Q(dureePreparation__icontains=keyword)
        )
    else:
        recipes = Recette.objects.all()

    return render(request, 'search_recipes.html', {'recipes': recipes})


