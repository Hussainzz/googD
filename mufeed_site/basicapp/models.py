from django.db import models
from django.core.urlresolvers import reverse


class Course(models.Model):
    name = models.CharField(max_length=256)
    lecturer = models.CharField(max_length=256)
    level = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basicapp:detail", kwargs={'pk':self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    course = models.ForeignKey(Course, related_name='students')

    def get_absolute_url(self):
        return reverse("basicapp:list")

    def __str__(self):
        return self.name
