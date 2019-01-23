from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, get_object_or_404


def activate(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/login/')
    return redirect('/')
