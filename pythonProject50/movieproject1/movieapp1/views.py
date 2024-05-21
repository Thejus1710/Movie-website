from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Movie, MovieRating
from django.contrib.auth.decorators import login_required


# Create your views here.
def registration(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname',)
        lastname = request.POST.get('lastname', )
        email = request.POST.get('email', )
        password = request.POST.get('password', )
        user=User(firstname=firstname,lastname=lastname,email=email,password=password)
        user.save()
    return render(request,'registration.html')

def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie

    }
    return render(request,'index.html',context)
def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        trailer= request.POST.get('trailer',)
        actors=request.POST.get('actors',)
        movie=Movie(name=name,desc=desc,year=year,image=image,trailer=trailer,actors=actors)
        movie.save()
    return render(request,'add.html')

def home(request):
    movie=Movie.objects.all()
    print(request.session.get("user_id"))
    context={
        'movie_list':movie

    }
    return render(request,'home.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    rate=MovieRating.objects.filter(movie=movie_id)
    return render(request,'rating.html',{'movie':movie,'rate':rate})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == 'POST':
        email = request.POST.get('email', )
        password = request.POST.get('password', )
        if User.objects.filter(email=email, password=password).exists():
            movie = Movie.objects.all()
            context = {
                'movie_list': movie

            }

            request.session["user"] = User.objects.filter(email=email, password=password).first().id

            return render(request, 'home.html',context)
        else:
            return HttpResponse('Invalid email or password')
def rate(request, movie_id):
    if request.method=='POST':
        rating=request.POST.get('rate',)
        movie = request.POST.get('movie', )
        user=request.session.get('user')
        print(rating,movie,user)
        MovieRating.objects.create(rating=rating,movie_id=movie,user_id=user)
        redirect_path = reverse('rate', kwargs={'movie_id': movie_id})

        return redirect(redirect_path)
