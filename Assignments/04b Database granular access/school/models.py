from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey("Campus", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    major = models.ManyToManyField("Major", related_name="courses")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    major = models.ForeignKey("Major", on_delete=models.CASCADE)
    courses = models.ManyToManyField("Course", related_name="students")

    def __str__(self):
        return self.name
