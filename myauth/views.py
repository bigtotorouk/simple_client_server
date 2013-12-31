# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

def register_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        terms = request.POST.get('terms', False)
        print 'term is ', terms

        # How check if user exists in Django
        if User.objects.filter(username=username).count():
            error = "The %s has already been registered.Please use other username to register." % username
        else:
            user = User.objects.create_user(username, email ,password)
            return HttpResponse("register success")

    return render_to_response('myauth/register.html', {'error': error}, context_instance=RequestContext(request))


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/index')
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=username, password=pwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponse("login success")
            else:
                # Return a 'disabled account' error message
                error = "An disabled account"
        else:
            # Return an 'invalid login' error message.
            error = "Invalid login"

    return render_to_response('myauth/login.html', {'error': error}, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponse('logout success')

def index(request):
    return render_to_response('index.html',{}, context_instance=RequestContext(request))

import json
def test_post(request):
    try:
        print request.raw_post_data
        data = json.loads(request.raw_post_data)
        print data
    except:
        print 'nope'
    return HttpResponse("{'result':'success'}",)