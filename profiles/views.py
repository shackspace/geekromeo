from django.views.generic import ListView

from .models import Profile

class ProfileHomeView(ListView):
    template_name = "profiles/profile_list.html"
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileHomeView, self).get_context_data(
            **kwargs)
        print dir(context['profile_list'])
        return context
