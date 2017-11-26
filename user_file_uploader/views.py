from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url="/user/login/")
def dashboard(request):
    return HttpResponseRedirect('/user/profile/%s' % request.user.username)

@login_required(login_url="/user/login/")
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'dashboard.html', { 'user': user })