from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
p_type = (
    ('web','web'),
    ('telegam','telegram'),
    ('desktop','desktop')
)



# Create your models here.
class Home_page_model(models.Model):
    logo = models.ImageField(upload_to = 'img/', blank=True)
    header_img = models.ImageField(upload_to = 'img/', blank=True)
    # my_img_mobile = models.ImageField(upload_to='img/', blank=True)
    my_name = models.CharField(max_length=155)
    my_subject = models.CharField(max_length=150)
    about_us = RichTextField()
    # about_us_img = models.ImageField(upload_to='img/', blank=True)
    # contact_photo = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return self.my_name


class Cantact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    my_resume = models.FileField(upload_to='pdf')
    telegram_username = models.CharField(max_length=300)
    
    telegram_url = models.CharField(max_length=300)
    facebook_url = models.CharField(max_length=300)
    instagram_url = models.CharField(max_length=300)
    linkedin_url = models.CharField(max_length=300)
    github_url = models.CharField(max_length=300)
    
    motivation_title = models.CharField(max_length=100)
    motivation_body = RichTextField()
    motivation_author = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Resume_education(models.Model):
    edu_date = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    edu_body = RichTextField()
    
    def __str__(self):
        return self.education +'  -->>  '+ self.edu_date
    
    
    
class Resume_certificate(models.Model):
    
    certificate_date = models.CharField(max_length=100)
    cartificate_name = models.CharField(max_length=255)
    certificate_body = RichTextField()
    certificate = models.FileField(upload_to='pdf', blank=True)
    
    
    def __str__(self):
        return self.cartificate_name +'  -->>  '+ self.certificate_date
    
    

class Portfolio(models.Model):
    project_name = models.CharField(max_length=150)
    project_body = RichTextField()
    project_link = models.CharField(max_length=250, blank=True)
    project_img = models.ImageField(upload_to = 'img/', blank=True)
    project_type = models.CharField(max_length=30, null=True, choices=p_type)
    
    def __str__(self):
        return self.project_name +'  -->>  '+ self.project_type
    
    
class Articles(models.Model):
    article_title = models.CharField(max_length=255)
    article_subtitle = RichTextField()
   
    article_body = RichTextField()
    article_img_1 = models.ImageField(upload_to='img/', blank=True)
    article_img_2 = models.ImageField(upload_to='img/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_title
    
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Skills(models.Model):
    skill_group = models.CharField(max_length=100)
    skills = models.TextField()
    
    
    def __str__(self):
        return self.skill_group
    



class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    body  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name +"  -  "+ self.date