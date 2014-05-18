from django.http import HttpResponse
from django.shortcuts import render_to_response
from article.models import Article 
 
def articles(request):
	language = 'en-gb'
	session_language = 'en-gb'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('articles.html',
								{'articles':Article.objects.all(),
								 'language':language, 
								 'session_language':session_language,
								 })

def article(request , article_id=1):
	return render_to_response('article.html',
								{'article':Article.objects.get(id=article_id) })

def language(request, language='en-gb'):
	response = HttpResponse("Setting language to %s" % language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response




def sample_advanced_url(request):
	html = "<html>Hi , This is an example for advanced URL</html>"
	return HttpResponse(html)