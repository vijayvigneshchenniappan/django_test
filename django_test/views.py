from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.core.context_processors import csrf
# Create your views here.

def hello(request):
	name = 'Vijay'
	html = "<html><body>Hi %s , This is Just Rocking </body></html>" %name
	return HttpResponse(html)

def hello_template(request):
	name = 'Vijay Vignesh'
	t = get_template('hello.html')
	html = t.render(Context({
			'name':name
		}))
	return HttpResponse(html)

def hello_template_simple(request):
	name = "Vj"
	return render_to_response('hello.html',{
		'name':name
		})


def login(request):
    c = {}
    c.update(csrf(request))    
    return render_to_response('login.html', c)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
