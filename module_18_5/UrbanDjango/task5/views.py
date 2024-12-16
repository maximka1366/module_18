from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister


users = ['Максим', 'Ольга', 'Денис', 'Николай', 'Петр']

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get('age')

        if password == repeat_password and int(age) >= 18 and username not in users:
            welcome = f'Приветствуем, {username}!'
            info['welkom'] = welcome

        elif password != repeat_password:
            error_password = "Пароли не совпадают"
            info['error_password'] = error_password
            if int(age) < 18:
                error_age = "Вы должны быть старше 17"
                info['error_age'] = error_age
                if username in users:
                    error_username = "Пользователь уже существует"
                    info['error_username'] = error_username
            elif username in users:
                error_username = "Пользователь уже существует"
                info['error_username'] = error_username

        elif int(age) < 18:
            error_age = "Вы должны быть старше 18"
            info['error_age'] = error_age
            if username in users:
                error_username = "Пользователь уже существует"
                info['error_username'] = error_username

        elif username in users:
            error_username = "Пользователь уже существует"
            info['error_username'] = error_username



    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data['age']
            subscribe = form.cleaned_data['subscribe']

            if password == repeat_password and int(age) >= 18 and username not in users:
                welcome = f'Приветствуем, {username}!'
                info['welkom'] = welcome

            elif password != repeat_password:
                error_password = "Пароли не совпадают"
                info['error_password'] = error_password
                if int(age) < 18:
                    error_age = "Вы должны быть старше 17"
                    info['error_age'] = error_age
                    if username in users:
                        error_username = "Пользователь уже существует"
                        info['error_username'] = error_username
                elif username in users:
                    error_username = "Пользователь уже существует"
                    info['error_username'] = error_username

            elif int(age) < 18:
                error_age = "Вы должны быть старше 18"
                info['error_age'] = error_age
                if username in users:
                    error_username = "Пользователь уже существует"
                    info['error_username'] = error_username

            elif username in users:
                error_username = "Пользователь уже существует"
                info['error_username'] = error_username

    else:
        form = UserRegister()

    info["form"] = form
    return render(request, 'fifth_task/registration_page.html', info)
