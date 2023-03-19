from django.forms import ModelForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class QuizForm(ModelForm):

    required_css_class = 'required'
    class Meta:
        model = QuizModel
        fields = ('__all__')

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuizModel
        fields="__all__"