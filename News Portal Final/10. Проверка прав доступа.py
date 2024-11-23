from django.contrib.auth.mixins import UserPassesTestMixin  

class PostCreateView(UserPassesTestMixin, CreateView):  
    model = Post  
    ...  

    def test_func(self):  
        return self.request.user.groups.filter(name='authors').exists() 