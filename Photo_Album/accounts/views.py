from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from Photo_Album.accounts.forms import UserCreateForm

UserModel = get_user_model()
class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    #TODO: have to add revers lazy to some page
    success_url = reverse_lazy('')