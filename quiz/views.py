from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.views.generic.edit import CreateView

def list(request):
    quiz_list = QuizModel.objects.all()
    themes = Theme.objects.all()
    context = {
        'quiz_list': quiz_list,
        'themes': themes,
    }
    return render(request, 'quiz_tem/list.html', context)

def quiz(request, theme_id):
    if request.method == 'POST':
        questions = QuizModel.objects.filter(theme=theme_id)
        themes = Theme.objects.all()
        curr_theme = Theme.objects.get(pk=theme_id)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            if q.ans == request.POST.get(q.ans):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'questions': questions,
            'themes': themes,
            'curr_theme': curr_theme,
        }
        return render(request,'quiz_tem/results.html',context)
    else:
        questions = QuizModel.objects.filter(theme=theme_id)
        themes = Theme.objects.all()
        curr_theme = Theme.objects.get(pk=theme_id)
        context = {
            'questions': questions,
            'themes': themes,
            'curr_theme': curr_theme,
        }
        return render(request, 'quiz_tem/quiz.html', context)
 
def create(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list/')

    context = {'form': form}
    return render(request, 'create.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('quiz') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'registration/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/list')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/list')
       context={}
       return render(request,'registration/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/list')


