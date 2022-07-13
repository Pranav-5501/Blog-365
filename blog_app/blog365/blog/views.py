import imp
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.models import Category
from blog.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def home(request):
    #load posts
    Posts = Post.objects.all()[:5:-1]

    cats = Category.objects.all()

    data = {
        'Posts':Posts,
        'cats' : cats
    }
    return render(request, 'home.html', data)

def post(request, url):
    pst = Post.objects.get(url=url)
    cats = Category.objects.all()[:6]
    return render(request,'posts.html', {'pst':pst,'cats':cats})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat':cat, 'posts':posts})

def contact(request):
    #form = ContactForm() 
    return render(request, 'contact.html', {})

def sendmail(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        email = request.POST.get('email',)
        subject = request.POST.get('subject',)
        message = request.POST.get('message',)

        send_mail(
            #name,
            #email,
            subject,
            message,
            'superuser.blog365@yahoo.com',
            ['contact.blog365@yahoo.com'],
            fail_silently=False,
        )
        #message.info(request,"Message send successfully")
        return render(request, '../home.html')

    else:
        #message.info(request,"Message not sent")
        return render(request, '../home.html')
