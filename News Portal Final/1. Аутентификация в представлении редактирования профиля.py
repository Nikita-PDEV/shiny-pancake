from django.contrib.auth.mixins import LoginRequiredMixin  
from django.views.generic import UpdateView  

class ProfileUpdateView(LoginRequiredMixin, UpdateView):  
    model = User  
    fields = ['username', 'email', 'first_name', 'last_name']  
    template_name = 'profile_update.html' 