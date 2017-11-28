from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import File, UserSharedFiles

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

    user_id = User.objects.get(username=username).id
    shared_file_ids = UserSharedFiles.objects.filter(shared_user_id=user_id).values('file_id')
    shared_files=[]
    for shared_file_id in shared_file_ids:
        pk = shared_file_id['file_id']
        shared_files.append(File.objects.get(pk=pk))
    return render(request, 'dashboard.html', { 'user': user, 'files': uploaded_files, 'shared_files': shared_files})


def get_user_uploaded_files(user_profile):
    return user_profile.file_set.all()

def get_user_profile(username):
    return User.objects.get(username=username).userprofile


def search(request):
    search_val = request.GET.get('search', None)

    if search_val is not None:
        users = User.objects.filter(username__icontains=search_val)
        user_names = []
        for user in users:
            user_names.append(user.username)

        return JsonResponse({ 'result' : user_names })
    else:
        return render(request, 'search.html')


def all(request):
    username = request.GET.get('username')
    users = User.objects.exclude(username=username)
    user_names = []
    for user in users:
        user_names.append(user.username)

    return JsonResponse({ 'result' : user_names })


def share_file(request):
    requested_user_id = request.user.id
    shared_user_name = request.POST.get('file_shared_with')
    shared_user = User.objects.filter(username=shared_user_name)
    file_id = int(request.POST.get('file_id'))

    if shared_user.count() > 0:
        shared_user_id = shared_user[0].id
        UserSharedFiles(file_id=file_id, requested_user_id=requested_user_id, shared_user_id=shared_user_id).save()
        return HttpResponse('success')