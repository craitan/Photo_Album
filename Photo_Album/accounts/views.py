from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from Photo_Album.accounts.forms import UserCreateForm, LoginForm, UserEditForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('photo gallery')

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)

        return redirect(self.success_url)


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('photo gallery')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home page')


# TODO: have to fix this so other people cant see pictures

class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel


class UserEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('home page')
