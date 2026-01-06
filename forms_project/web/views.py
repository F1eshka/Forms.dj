from django.shortcuts import render
from .forms import LoginForm, CalcForm, RegisterForm, YearForm
from datetime import date, timedelta
import locale

MENU = [
    {'url': '/', 'name': 'Главная'},
    {'url': '/login/', 'name': '1. Вход'},
    {'url': '/calc/', 'name': '2. Калькулятор'},
    {'url': '/register/', 'name': '3. Регистрация'},
    {'url': '/programmer/', 'name': '4. День программиста'},
]

def index(request):
    return render(request, 'web/base.html', {'menu': MENU, 'title': 'Главная'})

def user_login(request):
    result = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            if user == 'admin' and pwd == 'admin':
                result = f"Здравствуйте, Администратор {user}!"
            elif user == 'user' and pwd == '123':
                result = f"Привет, Пользователь {user}."
            else:
                result = "Неверный логин или пароль."
    else:
        form = LoginForm()
    
    return render(request, 'web/form_page.html', {'form': form, 'result': result, 'menu': MENU, 'title': 'Вход'})

def calc(request):
    result = None
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['num1']
            n2 = form.cleaned_data['num2']
            n3 = form.cleaned_data['num3']
            op = form.cleaned_data['operation']
            
            numbers = [n1, n2, n3]
            if op == 'min':
                result = f"Минимум: {min(numbers)}"
            elif op == 'max':
                result = f"Максимум: {max(numbers)}"
            elif op == 'avg':
                result = f"Среднее: {sum(numbers) / 3:.2f}"
    else:
        form = CalcForm()
        
    return render(request, 'web/form_page.html', {'form': form, 'result': result, 'menu': MENU, 'title': 'Калькулятор'})

def register(request):
    data = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form = RegisterForm()
        
    return render(request, 'web/register_result.html', {'form': form, 'data': data, 'menu': MENU})

def programmer_day(request):
    result = None
    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            start_date = date(year, 1, 1)
            prog_day = start_date + timedelta(days=255)
            days_ru = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
            weekday = days_ru[prog_day.weekday()]
            months_ru = ["", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
            month_name = months_ru[prog_day.month]
            
            result = f"{prog_day.day} {month_name} ({weekday})"
    else:
        form = YearForm()
        
    return render(request, 'web/form_page.html', {'form': form, 'result': result, 'menu': MENU, 'title': 'День программиста'})