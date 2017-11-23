from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def dashboard(request):
    context = { 'user_name': request.user.username }
    return render(request, 'dashboard.html', context)