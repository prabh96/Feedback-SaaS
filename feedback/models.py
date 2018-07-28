from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
	pub_name=models.CharField(max_length=200,default='test')
	url_text=models.CharField(max_length=200,unique=True)
	def __str__(self):
		return self.url_text

class Affective(models.Model):
	url = models.ForeignKey(Url, on_delete=models.CASCADE, null=True, related_name='affectives')
	user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	B="Boring"
	C="Confusing"
	E="Engaging"
	Affective_choices=((B,"Boring"),(C,"Confusing"),(E,"Engaging"),)
	affective = models.CharField(max_length=9,choices=Affective_choices,default="Boring")
	def __str__(self):
		return self.affective


class Cognitive(models.Model):
	url = models.ForeignKey(Url, on_delete=models.CASCADE, null=True, related_name='cognitives')
	user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	D="Difficult"
	E="Easy"
	Cognitive_choices=((D,"Difficult"),(E,"Easy"),)
	cognitive = models.CharField(max_length=9,choices=Cognitive_choices,default="Difficult")
	def __str__(self):
		return self.cognitive