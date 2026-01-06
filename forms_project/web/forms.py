from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=100)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

class CalcForm(forms.Form):
    num1 = forms.IntegerField(label="Число 1")
    num2 = forms.IntegerField(label="Число 2")
    num3 = forms.IntegerField(label="Число 3")
    
    CHOICES = [
        ('min', 'Минимум'),
        ('max', 'Максимум'),
        ('avg', 'Среднее арифметическое'),
    ]
    operation = forms.ChoiceField(label="Выберите действие", choices=CHOICES, widget=forms.RadioSelect)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    age = forms.IntegerField(label="Возраст", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    
    GENDER_CHOICES = [('m', 'Мужской'), ('f', 'Женский')]
    gender = forms.ChoiceField(label="Пол", choices=GENDER_CHOICES)
    
    address = forms.CharField(label="Адрес доставки", widget=forms.Textarea(attrs={'rows': 3}))
    subscribe = forms.BooleanField(label="Бажаєте підписатися на новини нашого інтернет-магазину?", required=False)

class YearForm(forms.Form):
    year = forms.IntegerField(label="Введите год", min_value=1)