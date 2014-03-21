from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from pasteapp.models import Paste
from django.contrib import auth

from django.contrib.auth.forms import UserCreationForm
import random
import string
from django import forms




def main(request):
	if request.method=='POST':
		content=request.POST.get('content','')
		title=request.POST.get('title','')
		created_on=request.POST.get('created_on','')

	
		char_set = string.ascii_uppercase + string.digits+string.ascii_lowercase
		url=''.join(random.sample(char_set*6,6))

     

		code=""
	else:
		return render(request,'index.html')
	

	
	if content:
		
		try:
			Paste.objects.get(url=url)
		except:
			if request.user.is_authenticated():
				p=Paste(content=content,url=url,title=title,created_on=created_on,user=request.user.username)
			else:
				p=Paste(content=content,url=url,title=title,created_on=created_on)

			
			p.save()
			code=content
			addr='http://%s/%s' %(request.get_host(),url)

	return render(request,'show.html',{'addr':addr,'code':code,'title':title})

def fetch_paste(request,offset):
	url=request.META.get('PATH_INFO','')[1:]
	content=""
	title=""

	
	try:
		p=Paste.objects.get(url=offset)

	except:
		error="http://%s/%s does not exists"%(request.get_host(),offset)
		return render(request,'pastedisplay.html',{'error':error})

	return render(request,'pastedisplay.html',{'p':p})


		
def login(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			return HttpResponseRedirect('/')
		else:
			error="Username or password did not match"
			return HttpResponseRedirect("/account/invalid")
	else:
		return render(request,'login.html')

    

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/account/login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def userhistory(request):
	if request.user.is_authenticated():
		try:
			print "reached try"
			p=Paste.objects.all().filter(user=request.user.username)
		except:
			print "error of userhistory"
			error="You have not made any paste"
			return render(request,'history.html',{'error':error})
		url=request.get_host()
		return render(request,'history.html',{'p':p,'url':url})
	else:
		error="You are not logged in"
		return render(request,'history.html',{'error':error})
	

def invalid(request):
	return render(request,'login.html',{'error':"Username or Password did not matched"})

def index(request):
	return render(request,'index.html')

def search(request):
	if request.method=='POST':
		q=request.POST.get('query','')
		url=request.get_host()

		try:
			paste=Paste.objects.all().filter(title=q)
		except:
			error="No results for %s" %q
			return render(request,'search_results.html',{'error':error})
		return render(request,'search_results.html',{'paste':paste,'query':q,'url':url})
	error="You did not search for anything"
	return render(request,'search_results.html',{'error':error})

	

