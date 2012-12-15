from django.views.generic import ListView, DetailView

from .models import Profile

class ProfileHomeView(ListView):
    model = Profile

class ProfileView(DetailView):
    model = Profile
    slug_field = 'user__username'
