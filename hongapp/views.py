from django.shortcuts import render
from django.http import HttpResponse
from .models import Hong
from django.core.paginator import Paginator
from django.utils import timezone
import hashlib

def main(request):
    page = request.GET.get('page', '')
    if not page: page = '1'
    page = int(page)

    prd = request.GET.get('prd', '')
    hong = Hong.objects.filter(name__contains=prd).order_by('id')
    p = Paginator(hong, 10)

    s_page = (page - 1) // 10 * 10 + 1
    e_page = s_page + 9
    pages = range(s_page, e_page + 1)

    return render(request, "hongapp/main.html", 
                    {
                      "hong": p.page(page),
                      'pages': pages,
                      'page': page
                    }
                )









# def user_signup(request):
#     #POST 로 요청했을 때
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         name = request.POST.get('name')
#         pwd = request.POST.get('pwd')
#         u = User()
#         u.email = email
#         u.name = name
#         u.pwd = encrypt(pwd)
#         u.c_date = timezone.now()
#         u.save()

#         return HttpResponse('%s님 가입 감사합니다.' % name)
#     #GET 으로 요청했을 때
#     return render(request, 'firstapp/signup.html', {})

# def encrypt(pwd):
#     m = hashlib.sha256()
#     m.update(pwd.encode('utf-8'))
#     new_pwd = m.hexdigest()
#     return new_pwd
