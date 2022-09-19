from django.contrib import admin
from .models import Home_page_model, Cantact, Resume_education, Resume_certificate, Portfolio, Articles, Skills, Message
# Register your models here.
admin.site.register(Home_page_model)

admin.site.register(Cantact)
admin.site.register(Resume_education)
admin.site.register(Resume_certificate)
admin.site.register(Portfolio)
admin.site.register(Articles)
admin.site.register(Skills)
admin.site.register(Message)
