from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import File

@login_required(login_url="/user/login/")
def dashboard(request):
    return HttpResponseRedirect('/user/profile/%s' % request.user.username)

@login_required(login_url="/user/login/")
def get_user_profile_view(request, username):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        user_profile = get_user_profile(username)
        file = File(user=user_profile,
                    file_name=myfile.name,
                    file=myfile,
                    created_at=timezone.now())
        file.save()

        uploaded_files = get_user_uploaded_files(user_profile)
        return render(request, 'dashboard.html', { 'files': uploaded_files })

    user = User.objects.get(username=username)
    uploaded_files = get_user_uploaded_files(user.userprofile)
    return render(request, 'dashboard.html', { 'user': user, 'files': uploaded_files })


def get_user_uploaded_files(user_profile):
    return user_profile.file_set.all()

def get_user_profile(username):
    return User.objects.get(username=username).userprofile
