from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/')
    about = models.TextField()

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    hero_description = models.TextField(blank=True, null=True)

    github = models.URLField()
    linkedin = models.URLField()

    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    percentage = models.IntegerField()
    icon = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to='project/')

    description = models.TextField()

    technologies = models.CharField(max_length=200)

    github_url = models.URLField()
    live_url = models.URLField(unique=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    qualification = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    score = models.CharField(max_length=20)


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_phone = models.CharField(max_length=15)
    emp_salary = models.DecimalField(max_digits=10,decimal_places=2)
    emp_address = models.TextField()

    def __str__(self):
        return self.emp_name


