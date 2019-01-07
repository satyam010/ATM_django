from django.db import models

# Create your models here.
class logininfo(models.Model):
	user_name=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	balance=models.IntegerField(default=0)

	def __str__(self):
		return self.user_name+" "+self.password+" "+str(self.balance)


class ministatement(models.Model):
	amount=models.IntegerField(default=0)
	type=models.CharField(max_length=30)
	user_name=models.CharField(max_length=30)
	abalance=models.IntegerField(default=0)
	tdate=models.CharField(max_length=30)

	def __str__(self):
		return str(self.amount)+" "+self.type+" "+self.user_name+" "+str(self.abalance)+" "+self.tdate