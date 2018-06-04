from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# import time
from .models import Chat



def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # WelcomeUser(user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect('/login/')
    return render(request, "alpha/login.html")


def Logout(request):
    # logout(request)
    Chat.objects.all().delete()
    return HttpResponseRedirect('/login/')


def Home(request):
    c = Chat.objects.all()
    return render(request, "alpha/home.html", {'chat': c})


def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox')

        c = Chat(user=request.user, message=msg)

        # if(msg[0:6] == "Robot:"):
        # callRobot(msg, request)

        msg = c.user.username + ": " + msg

        c = Chat(user=request.user, message=msg)

        if msg != '':
            c.save()
        # mg = src="https://scontent-ord1-1.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/p160x160/11070096_10204126647988048_6580328996672664529_n.jpg?oh=f9b916e359cd7de9871d8d8e0a269e3d&oe=576F6F12"
        return JsonResponse({'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')


def Messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})

