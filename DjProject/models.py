from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=10,choices=g) 
	impf = models.ImageField(upload_to="Profile/",default="profile.jpeg") 

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)
# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	description = models.TextField()

	def __str__(self):
		return self.name +" - " + self.email