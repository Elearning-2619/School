from django.db import models
from django.utils.text import slugify

class Student(models.Model):
	std_name = models.CharField(max_length = 100, db_index = True)
	std_rollno = models.CharField(max_length=30)
	slug = models.SlugField(max_length = 100, unique = True)
	address = models.TextField(max_length = 100, blank = True)
	image = models.ImageField(null=True, blank = True)
	std_entry = models.DateTimeField(auto_now_add = True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.std_rollno) + '-' + slugify(self.std_entry)
		super(Student, self).save(*args, **kwargs)

	class Meta:
		ordering = ('-std_name',)

	def __str__(self):
		return self.std_name