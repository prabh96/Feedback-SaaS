from django.urls import path

from . import views

urlpatterns = [
	path('create_url/',views.create_url,name='create_url'),
	path('submit_affective/',views.submit_affective,name='submit_affective'),
	path('submit_cognitive/',views.submit_cognitive,name='submit_cognitive'),
	path('thanks/',views.thanks,name='thanks'),
	path('detail_affective/<int:id>',views.detail_affective,name='detail_affective'),
	path('detail_cognitive/<int:id>',views.detail_cognitive,name='detail_cognitive'),
	path('register/',views.register,name='register'),
	path('<int:id>',views.index,name='index'),
]