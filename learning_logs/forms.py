from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comentario

class FormularioDeRegistro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help_texts padrão
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        # Labels em português
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'

        # Mensagens de erro personalizadas para cada campo, se quiser:
        self.fields['username'].error_messages = {
            'required': 'O nome de usuário é obrigatório.',
            'unique': 'Este nome de usuário já está em uso.',
            'max_length': 'Use até 150 caracteres.',
        }
        self.fields['password1'].error_messages = {
            'required': 'A senha é obrigatória.',
        }
        self.fields['password2'].error_messages = {
            'required': 'Você precisa confirmar a senha.',
        }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        """
        Aqui substituímos a validação padrão de 'password_mismatch'
        para usar nossa mensagem em português.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "As senhas não coincidem.", code='password_mismatch'
            )
        return password2

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite seu comentário...'}),
        }
