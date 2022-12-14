# Generated by Django 4.1 on 2022-08-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=255)),
                ('article_subtitle', models.TextField()),
                ('article_body', models.TextField()),
                ('article_img_1', models.ImageField(blank=True, upload_to='img/')),
                ('article_img_2', models.ImageField(blank=True, upload_to='img/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=500)),
                ('my_resume', models.FileField(upload_to='pdf')),
                ('telegram_username', models.CharField(max_length=300)),
                ('telegram_url', models.CharField(max_length=300)),
                ('facebook_url', models.CharField(max_length=300)),
                ('instagram_url', models.CharField(max_length=300)),
                ('linkedin_url', models.CharField(max_length=300)),
                ('github_url', models.CharField(max_length=300)),
                ('motivation_title', models.CharField(max_length=100)),
                ('motivation_body', models.TextField()),
                ('motivation_author', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Home_page_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='img/')),
                ('header_img', models.ImageField(blank=True, upload_to='img/')),
                ('my_name', models.CharField(max_length=155)),
                ('my_subject', models.CharField(max_length=150)),
                ('about_us', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150)),
                ('project_body', models.TextField()),
                ('project_link', models.CharField(blank=True, max_length=250)),
                ('project_img', models.ImageField(blank=True, upload_to='img/')),
                ('project_type', models.CharField(choices=[('web', 'web'), ('telegam', 'telegram'), ('desktop', 'desktop')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_date', models.CharField(max_length=100)),
                ('cartificate_name', models.CharField(max_length=255)),
                ('certificate_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_date', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=255)),
                ('edu_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_group', models.CharField(max_length=100)),
                ('skills', models.TextField()),
            ],
        ),
    ]
