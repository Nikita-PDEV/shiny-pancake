from django.contrib.auth.models import Permission  
from yourapp.models import Post  

# Привязывание прав к группе authors  
def assign_permissions_to_authors():  
    authors_group = Group.objects.get(name='authors')  
    permissions = [  
        'add_post',  
        'change_post',  
        'delete_post',  
    ]  
    for perm in permissions:  
        permission = Permission.objects.get(codename=perm)  
        authors_group.permissions.add(permission)  