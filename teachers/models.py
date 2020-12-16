from django.db import models

class Teacher(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField()
    email = models.EmailField()
    grade = models.IntegerField(default=16)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name