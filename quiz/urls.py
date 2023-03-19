from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('list/', list, name='list'),
    path('list/<int:theme_id>/', quiz, name='quiz'),
    path('quiz/create/', create, name='create'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
]