from django.urls import path
from .import views
from .views import *


app_name = "movieapp"
urlpatterns = [
    path('',HomeView.as_view(),name = "home"),
    path('allmovies/',MovieView.as_view(),name="movie"),
    path('allmovies-rate/',views.rate_allmovies,name = 'rate_allmovies'),
    path('contact/',views.contact, name= "contact"),
    path('comedy/',ComedyView.as_view(),name="comedy"),
    path('action/',ActionView.as_view(),name = "action"),
    path('adventure/',AdventureView.as_view(),name = "adventure"),
    path('animation/',AnimationView.as_view(),name = "animation"),
    path('crime/',CrimeView.as_view(),name = "crime"),
    path('documentary/',DocumentaryView.as_view(),name = "documentary"),
    path('drama/',DramaView.as_view(),name = "drama"),
    path('family/',FamilyView.as_view(),name = "family"),
    path('fantasy/',FantasyView.as_view(),name = "fantasy"),
    path('fantasy-rate/',views.rate_fantasy,name = 'rate_fantasy'),
    path('history/',HistoryView.as_view(),name = "history"),
    path('horror/',HorrorView.as_view(),name = "horror"),
    path('musical/',MusicalView.as_view(),name = "musical"),
    path('sciencefiction/',ScienceFictionView.as_view(),name = "sciencefiction"),
    path('romance/',RomanceView.as_view(),name = "romance"),
    path('thriller/',ThrillerView.as_view(),name = "thriller"),
    path('war/',WarView.as_view(),name = "war"),
    path('western/',WesternView.as_view(),name = "western"),
    path('tvmovie/',TVMovieView.as_view(),name="tvmovie"),
    path('mystery/',MysteryView.as_view(),name = "mystery"),
    path('foreign/',ForeignView.as_view(),name ="foreign"),
   
  
    path('search/',views.search,name ="search"),
    path('login/',views.loginPage,name = "login"),
    path('register/',views.registerPage,name = "register"),
    path('logout/',views.logoutUser,name="logout"),
    
    path('moviedetails/',MovieDetailView.as_view(),name = 'moviedetails'),
    path('practise/',views.practise,name = "practise")


    
]