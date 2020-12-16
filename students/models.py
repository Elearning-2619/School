from django.db import models

# Create your models here.
class Student(models.Model):
	std_name = models.CharField(max_length = 100, db_index = True)
	std_id = models.IntegerField(max_length = 50, unique = True)
	slug = models.SlugField(max_length = 100, unique = True)
	address = models.TextField(max_length = 100, blank = True)
	image = models.ImageField(upload_to = 'student/%Y/%m/%d', blank = True)
	std_entry = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ('-std_name',)

	def __str__(self):
		return self.std_entry
