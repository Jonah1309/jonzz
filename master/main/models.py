from django.db import models

class Cat(models.Model):
	cat_id=models.AutoField(primary_key=True)
	cat_name=models.CharField(max_length=200)

	def __str__(self):
		return self.cat_name

class Sub(models.Model):
	sub_id=models.AutoField(primary_key=True)
	sub_name=models.CharField(max_length=200)
	sub_cat_name=models.CharField(max_length=200)

	def __str__(self):
		return self.sub_name

class Act(models.Model):
	act_id=models.AutoField(primary_key=True)
	act_name=models.CharField(max_length=200)
	act_sub_name=models.CharField(max_length=200)
	act_cat_name=models.CharField(max_length=200)

	def __str__(self):
		return self.act_name

class Users(models.Model):
	us_id=models.IntegerField(primary_key=True)
	us_des=models.TextField()

	def __str__(self):
		return '%s %s' % (self.us_id,self.us_des)