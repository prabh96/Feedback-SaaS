from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from .models import Affective, Cognitive, Url
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from feedback.forms import SignUpForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse("Thanks for signing up. Please refresh the page.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def register(request):
	return render(request,'register1.html')


def create_url(request):
	if request.method == 'POST':
		pub_name=request.POST['pub_name']
		url_text=request.POST['url_name']
		try:
			url_result,created=Url.objects.get_or_create(
				pub_name=pub_name, url_text=url_text
				)
			a=url_result.id
			return HttpResponse("Please use the following code :<textarea>&lt;iframe src='http://127.0.0.1:8000/"+str(a)+"'"" width='600px' height='800px' style= 'visibility:visible' id= 'the_iframe'/&gt;</textarea>")
		except:
			return HttpResponseNotFound('A url with this name has already been registered.')
		#return redirect('index',url=url_text)
		

def submit_affective(request):
	if request.method == 'POST':
		urlaff=request.POST['f1']
		print(urlaff)
		urlobj=Url.objects.get(
			url_text=urlaff
			)
		print(urlobj.url_text)
		choice=request.POST['aff_choices']
		#urlid=request.POST['url_list']
		#urlid=urlobj.id
		userid=request.user.id
		user=User.objects.get(id=userid)
		#url = Url.objects.get(id=urlid)
		aff_result=Affective.objects.create(
			affective=choice, url=urlobj, user=user
			)
		return redirect('detail_affective',id=urlobj.id)

def submit_cognitive(request):
	if request.method == 'POST':
		urlcog=request.POST['f2']
		print(urlcog)
		urlobj=Url.objects.get(
			 url_text=urlcog
			)
		print(urlobj.url_text)
		choice=request.POST['cog_choices']
		userid=request.user.id
		user=User.objects.get(id=userid)
		cog_result=Cognitive.objects.create(
			cognitive=choice, url=urlobj, user=user
			)
		return redirect('detail_cognitive',id=urlobj.id)

@login_required
def index(request,id):
	url=Url.objects.get(pk=id)
	return render(request,'index.html',{'url':url})

def thanks(request):
	return HttpResponse('<i>Thank You</i>')

def detail_affective(request,id):
	boring_count=Affective.objects.filter(affective='Boring',url_id=id).count()
	confusing_count=Affective.objects.filter(affective='Confusing',url_id=id).count()
	engaging_count=Affective.objects.filter(affective='Engaging',url_id=id).count()
	url=Url.objects.get(pk=id)
	context = {
		'boring_count':boring_count,
		'confusing_count':confusing_count,
		'engaging_count':engaging_count,
		'url':url,
	}
	return render(request,'detail_affective.html',context)

def detail_cognitive(request,id):
	easy_count=Cognitive.objects.filter(cognitive='Easy',url_id=id).count()
	difficult_count=Cognitive.objects.filter(cognitive='Difficult',url_id=id).count()
	boring_count=Affective.objects.filter(affective='Boring',url_id=id).count()
	confusing_count=Affective.objects.filter(affective='Confusing',url_id=id).count()
	engaging_count=Affective.objects.filter(affective='Engaging',url_id=id).count()
	url=Url.objects.get(pk=id)

	context = {
	'easy_count':easy_count,
	'difficult_count':difficult_count,
	'boring_count':boring_count,
	'confusing_count':confusing_count,
	'engaging_count':engaging_count,
	'url':url,
    }
	return render(request,'detail_cognitive.html',context)
