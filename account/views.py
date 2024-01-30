from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import SignupForm, LoginForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('tasks:task_list')  # Correct the namespace here

    def form_valid(self, form):
        messages.success(self.request, f"Welcome, {self.request.user.username}!")
        return super().form_valid(form)

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'account/logout.html'
    next_page = reverse_lazy('tasks:task_list') 

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(self.request, "You have been logged out successfully.")
        return response


class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('tasks:task_list')  # Correct the namespace here

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Account created for {self.object.username}. You can now log in.")
        return response
