from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
# CRUD 
# Create, Update : 입력 받아야 하는 form이 존재 - form 태그 존재
# 지금까지는 폼을 자동으로 만들어 줬지만
# but 이번엔 수동으로 -> forms.py

def register(request):
    if request.method == "POST":
        # 회원 가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)     # user 클래스의 instance
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})

    else:
        # 회원 가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})