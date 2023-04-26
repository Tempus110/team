from django.shortcuts import render
from django.http import HttpResponse
from .models import Sleep, User
from django.utils import timezone
import hashlib

def main(request):
    sleep = Sleep.objects.all()

    return render(request, 'sleepapp/main.html', {'sleep': sleep})

def user_signup(request):
    #POST 로 요청했을 때
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        u = User()
        u.email = email
        u.name = name
        u.pwd = encrypt(pwd)
        u.c_date = timezone.now()
        u.save()

        return HttpResponse('%s님 가입 감사합니다.' % name)
    #GET 으로 요청했을 때
    return render(request, 'firstapp/signup.html', {})

def encrypt(pwd):
    m = hashlib.sha256()
    m.update(pwd.encode('utf-8'))
    new_pwd = m.hexdigest()
    return new_pwd