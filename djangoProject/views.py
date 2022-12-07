from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.loader import get_template

from .forms import CreateUserForm
from .forms import CreateCVForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CV
from django.http import HttpResponse, HttpResponseRedirect
import pdfkit

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, r'register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_cv')
        else:
            messages.info(request, 'Incorrect')

    context = {}
    return render(request, r'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def create_cvPage(request):
    form = CreateCVForm()
    if request.method == "POST":
        form = CreateCVForm(request.POST)
        if form.is_valid():
            print('Hooray')
            name = form.cleaned_data['name']
            skills = form.cleaned_data['skills']
            interests = form.cleaned_data['interests']
            education = form.cleaned_data['education']
            experience = form.cleaned_data['experience']
            #img = form.img
            model = CV(user=request.user,name=name, skills=skills, interests=interests, education=education, experience=experience)
            model.save()
            return HttpResponseRedirect('/cv_page/' + str(model.id))

    context = {'form' : form}
    return render(request, r'create_cv.html', context)

@login_required(login_url='login')
def cvPage(request, id):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    bio = CV.objects.get(id=id)
    print(bio.user, request.user)
    if str(bio.user) != str(request.user):
        return render(request, r'declined.html')
    template = get_template(r'cv_page..html')
    html = template.render({'cv' : bio})
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'
    return response
    #return render(request, r'cv_page..html', context={'cv' : bio})