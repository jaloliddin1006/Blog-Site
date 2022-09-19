from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Home_page_model,  Cantact, Resume_education, Resume_certificate, Portfolio, Articles, Skills, Message

def HomePageView(request):
 
    home_page = Home_page_model.objects.all()
    cantact = Cantact.objects.all()
    resume_education = Resume_education.objects.all()
    resume_certificate = Resume_certificate.objects.all()
    portfolio = Portfolio.objects.all()
    articles = Articles.objects.all()
    skills = Skills.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Message.objects.create(name=name, email = email, body = message).save()


    all_models = {
        'home_pagee':home_page, 
        'cantact':cantact,
        'resume_education':resume_education,
        'resume_certificate':resume_certificate,
        'portfolio':portfolio,
        'articles':articles,
        'skills':skills,
        }
    
    return render(request, 'index.html', all_models)



def ArticleDetailView(request, pk):
  

    cantact = Cantact.objects.all()
    
    articless = Articles.objects.all()
  
    articles = Articles.objects.get(pk=pk)
   
    all_models = {
      
        'cantact':cantact,
     
        'articles':articles,
        
        'articless':articless,
  
        }
    return render(request, 'article_detail.html', all_models)

class ArticleDetailView2(DetailView):
    model = Articles
    template_name = 'article_detail.html'