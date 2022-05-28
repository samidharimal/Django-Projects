from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.contrib import messages


from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
from django.db.models import Avg

# Create your views here.


class HomeView(ListView):
    model = PopularMovies
    template_name = "home.html"
    context_object_name = 'popularmovies'
    ordering = ['-id']
    paginate_by = 12
    




class ComedyView(ListView):
    model = Comedy
    template_name = "genres/comedy.html"
    context_object_name = 'comedymovies'
    paginate_by = 9


 
class ActionView(ListView):
    model = Action
    template_name = "genres/action.html"
    context_object_name = 'actionmovies'
    paginate_by = 9


class AdventureView(ListView):
    model = Adventure
    template_name = "genres/adventure.html"
    context_object_name = 'adventuremovies'
    paginate_by = 9

class AnimationView(ListView):
    model = Animation
    template_name = "genres/animation.html"
    context_object_name = 'animationmovies'
    paginate_by = 9



class CrimeView(ListView):
    model = Crime
    template_name = "genres/crime.html"
    context_object_name = 'crimemovies'
    paginate_by = 9



class DocumentaryView(ListView):
    model = Documentary
    template_name = "genres/documentary.html"
    context_object_name = 'documentarymovies'
    paginate_by = 9


class DramaView(ListView):
    model = Drama
    template_name = "genres/drama.html"
    context_object_name = 'dramamovies'
    paginate_by = 9
    

class FamilyView(ListView):
    model = Family
    template_name = "genres/family.html"
    context_object_name = 'familymovies'
    paginate_by = 9
    

class FantasyView(ListView):
    model = Fantasy
    template_name = "genres/fantasy.html"
    context_object_name = 'fantasymovies'
    paginate_by = 9
    ordering = ['-id']


def rate_fantasy(request): 
    if request.method == 'POST':
        fantasy_id = request.POST.get('fantacy_id')
        rating = request.POST.get('rating')
        print(fantasy_id, rating)
        fantacy_obj = Fantasy.objects.get(id= fantasy_id)
        # calculate rating
        if Review.objects.filter(fantasy=fantacy_obj, user=request.user).exists():
            return JsonResponse({'success': False})
        else:
            Review.objects.create(fantasy=fantacy_obj, user=request.user, rating=rating)
            reviews = fantacy_obj.review_set.all()
            avg_rating = reviews.aggregate(avg=Avg('rating'))
            fantacy_obj.rating = avg_rating.get("avg")
            fantacy_obj.save()  
        return JsonResponse({'success':'true','rating':rating},safe = False)
    return JsonResponse({'success':'false'})
 

class MovieView(ListView):
    model=MovieList
    template_name = "list.html"
    context_object_name = 'allmovies'
    ordering= ['-id']
    paginate_by = 12

def rate_allmovies(request): 
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        rating = request.POST.get('rating')
        print(movie_id, rating)
        movie_obj = MovieList.objects.get(id= movie_id)
        # calculate rating
        if MovieReview.objects.filter(movie=movie_obj, user=request.user).exists():
            return JsonResponse({'success': False})
        else:
            MovieReview.objects.create(movie=movie_obj, user=request.user, rating=rating)
            reviews = movie_obj.moviereview_set.all()
            avg_rating = reviews.aggregate(avg=Avg('rating'))
            movie_obj.rating = avg_rating.get("avg")
            movie_obj.save()  
        return JsonResponse({'success':'true','rating':rating},safe = False)
    return JsonResponse({'success':'false'})
   
             


class HistoryView(ListView):
    model = History
    template_name = "genres/history.html"
    context_object_name = 'historymovies'
    paginate_by = 9


class HorrorView(ListView):
    model = Horror
    template_name = "genres/horror.html"
    context_object_name = 'horrormovies'
    paginate_by = 9


class MusicalView(ListView):
    model = Music
    template_name = "genres/musical.html"
    context_object_name = 'musicalmovies'
    paginate_by = 9


class ScienceFictionView(ListView):
    model = ScienceFiction
    template_name = "genres/sciencefiction.html"
    context_object_name = 'sciencemovies'
    paginate_by = 9

class RomanceView(ListView):
    model = Romance
    template_name = "genres/romance.html"
    context_object_name = 'romancemovies'
    paginate_by = 9


class ThrillerView(ListView):
    model = Thriller
    template_name = "genres/thriller.html"
    context_object_name = 'thrillermovies'
    paginate_by = 9


class WarView(ListView):
    model = War
    template_name = "genres/war.html"
    context_object_name = 'warmovies'
    paginate_by = 9

class WesternView(ListView):
    model = Western
    template_name = "genres/western.html"
    context_object_name = 'westernmovies'
    paginate_by = 9

class TVMovieView(ListView):
    model = TVMovie
    template_name = "genres/tvmovie.html"
    context_object_name = "tvmovies"
    paginate_by = 9

class MysteryView(ListView):
    model = Mystery
    template_name = "genres/mystery.html"
    context_object_name = "mysterymovies"
    paginate_by = 9


class ForeignView(ListView):
    model = Foreign
    template_name = "genres/foreign.html"
    context_object_name = 'foreignmovies'
    paginate_by = 9






def practise(request):
    return render(request,"practise.html")


class MovieDetailView(TemplateView):
    template_name = 'moviedetails.html'






def registerPage(request):

    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was successfully created for' +user)
                return redirect('/login/')
        context = {'form':form}
        return render(request,'accounts/register.html',context)
            
  

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
       
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Username Or password is incorrect')
        context = {}
        return render(request,'accounts/login.html',context)   

def logoutUser(request):
    logout(request)
    return redirect('/login/')


def search(request):
    query = request.GET['query']
    actionmovies = Action.objects.filter(title__icontains = query)
    adventuremovies = Adventure.objects.filter(title__icontains = query)
    animationmovies = Animation.objects.filter(title__icontains = query)
    comedymovies = Comedy.objects.filter(title__icontains = query)
    crimemovies = Crime.objects.filter(title__icontains = query)
    documentarymovies = Documentary.objects.filter(title__icontains = query)
    dramamovies = Drama.objects.filter(title__icontains = query)
    familymovies = Family.objects.filter(title__icontains = query)
    
    foreignmovies = Foreign.objects.filter(title__icontains = query)
    historymovies = History.objects.filter(title__icontains = query)
    horrormovies = Horror.objects.filter(title__icontains = query)
    musicalmovies = Music.objects.filter(title__icontains = query)
    mysterymovies = Mystery.objects.filter(title__icontains = query)
    romancemovies = Romance.objects.filter(title__icontains = query)
    sciencemovies = ScienceFiction.objects.filter(title__icontains = query)
    thrillermovies = Thriller.objects.filter(title__icontains = query)
    tvmovies = TVMovie.objects.filter(title__icontains = query)
    warmovies = War.objects.filter(title__icontains = query)
    westernmovies = Western.objects.filter(title__icontains = query)

    params = {'actionmovies':actionmovies,'adventuremovies':adventuremovies,'animationmovies':animationmovies,'comedymovies':comedymovies,
    'crimemovies':crimemovies,'documentarymovies':documentarymovies,'dramamovies':dramamovies,'familymovies':familymovies,
   'foreignmovies':foreignmovies,'historymovies':historymovies,'horrormovies':horrormovies,
    'musicalmovies':musicalmovies,'mysterymovies':mysterymovies,'romancemovies':romancemovies,'sciencemovies':sciencemovies,
    'thrillermovies':thrillermovies,'tvmovies':tvmovies,'warmovies':warmovies,'westernmovies':westernmovies}
    paginator = Paginator(params, 10)  # 3 posts in each page
    return render(request,"search.html",params)

def contact(request):
    if request.method == "POST":
        contact=Contact()
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        
        description = request.POST.get('description','')
        print(name,email,description)
        
        contact = Contact(name=name, email=email,description=description)
        contact.save()
        messages.success(request,"your message has been successfully sent. ")

    return render(request,"contact.html")

   






