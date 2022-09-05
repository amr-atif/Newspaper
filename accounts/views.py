from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreation

class SignUp(CreateView):
    form_class= CustomUserCreation
    success_url=reverse_lazy('login')
    template_name='registration/register.html'