from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import registertbl


# Create your views here.
def home(request):
  return render(request, "home.html")


def login_view(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    # डेटाबेस से यूज़र को वेरीफाई करें
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, "Login Successful!")
      return redirect("home")  # सफल होने पर होमपेज पर भेजें
    else:
      messages.error(request, "Invalid Username or Password!")

  return render(request, "login.html")


def signup_view(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    if User.objects.filter(username=username).exists():
      messages.error(request, "Username already exists!")
    else:
      User.objects.create_user(username=username, password=password)
      messages.success(request, "Registration successful! Please login.")
      return redirect("/login/")

  return render(request, "signup.html")


def page(request):
  return render(request, "page.html")


def shopping(request):
  return render(request, "online shopping project.html")


def best(request):
  return render(request, "best selling.html")


def mobile(request):
  return render(request, "mobile.html")


def women(request):
  return render(request, "women.html")


def men(request):
  return render(request, "men.html")


def toy(request):
  return render(request, "toy.html")


def kid(request):
  return render(request, "kid.html")


def about(request):
  return render(request, "about.html")


def buy(request):
  return render(request, "buy now.html")

def contact(request):
  return render(request, "contact.html")


from django.db.models import Q
from django.shortcuts import render
from .models import Product  # (यहाँ ध्यान दें: अगर आपके models.py में नाम कुछ और है तो उसे यहाँ बदलें)


def search_view(request):
  query = request.GET.get('q', '')
  if query:
    keywords = query.split()
    conditions = Q()
    for word in keywords:
      conditions |= Q(name__icontains=word) | Q(description__icontains=word)

    products = Product.objects.filter(conditions).distinct()
  else:
    products = []

  return render(request, 'search.html', {'products': products, 'query': query})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message_text = request.POST.get('message')

    # डेटाबेस में सेव करें
    Contact.objects.create(
      name=name,
      email=email,
      subject=subject,
      message=message_text
    )

    messages.success(request, 'Your message has been sent successfully!')
    return redirect('contact')

  return render(request, 'contact.html')