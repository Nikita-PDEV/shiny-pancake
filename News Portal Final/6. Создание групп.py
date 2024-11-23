from django.contrib.auth.models import Group  

common_group, created = Group.objects.get_or_create(name='common')  
authors_group, created = Group.objects.get_or_create(name='authors') 