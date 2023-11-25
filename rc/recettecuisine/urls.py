from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path('',logIn, name="login"),
    path('Home/',Home, name="Home"),
    path('index/',Index, name="index"),
    path('create/',createRecipe, name="createRecipe"),
    path('update/<str:pk>/',updateRecipe, name="updateRecipe"),
    path('delete/<str:pk>/', deleteRecipe, name="deleteRecipe"),
    path('logout/',logOut, name="logout"),
    path('signup/',signUp, name="signup"),
    path('search_recipes/', search_recipes, name='search_recipes'),
    #path('recipe_list/', recipe_list, name="recipe_list"),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)