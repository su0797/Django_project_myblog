from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class JoinForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['name', 'email']



class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']
