from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=30, error_messages={
        'required': 'Campo Obrigatório',
        'max_length': 'O nome deve ser menor que 30 caracteres'
    })
    senha = forms.CharField(min_length=8, max_length=30, error_messages={
        'required': 'Campo Obrigatório',
        'max_length': 'A senha deve ser menor que 30 caracteres',
        'min_length': 'A senha deve ser maior que 8 caracteres'
    })

class LoginForm(forms.Form):
    nome = forms.CharField(max_length=30, error_messages={
        'required': 'Campo Obrigatório',
        'max_length': 'O nome deve ser menor que 30 caracteres'
    })
    senha = forms.CharField(min_length=8, max_length=30, error_messages={
        'required': 'Campo Obrigatório',
        'max_length': 'A senha deve ser menor que 30 caracteres',
        'min_length': 'A senha deve ser maior que 8 caracteres'
    })

