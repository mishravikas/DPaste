
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    
    #url(r'^pastebin/$','pasteapp.views.index'),
	url(r'^$','pasteapp.views.index'),
	url(r'^([a-zA-Z0-9]{1,6})$','pasteapp.views.fetch_paste'),
	url(r'^([A-Za-z]{1,6})$','pasteapp.views.fetch_paste'),
	url(r'^account/login$','pasteapp.views.login'),
	url(r'^account/register$','pasteapp.views.register'),
	url(r'^account/logout$','pasteapp.views.logout'),
	#url(r'^account/loggedin$','pasteapp.views.loggedin'),
	#url(r'^account/loggedout$','pasteapp.views.loggedout'),
	url(r'^account/invalid$','pasteapp.views.invalid'),
	url(r'^userhistory/$','pasteapp.views.userhistory'),
	#url(r'^account/newindex/$','pasteapp.views.newindex'),
	url(r'^paste/show/$','pasteapp.views.main'),
	url(r'^paste/search/$','pasteapp.views.search'),


	

	
)
