def become_author(user):  
    authors_group = Group.objects.get(name='authors')  
    user.groups.add(authors_group)  