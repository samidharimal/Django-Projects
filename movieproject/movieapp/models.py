from django.core import validators
from django.db import models
from django.db.models.fields import CharField, DateField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator







class MovieGenre(models.Model):
    genres = models.CharField(max_length= 100)



    def __str__(self):
        return self.genres

class Comedy(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
    

    def __str__(self):
        return self.title


class Animation(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
    

    def __str__(self):
        return self.title

class Family(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
    

    def __str__(self):
        return self.title

class Romance(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
    

    def __str__(self):
        return self.title

class Crime(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
    

    def __str__(self):
        return self.title
class Drama(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    
      

    def __str__(self):
        return self.title 


class Action(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
      
      

    def __str__(self):
        return self.title
class Thriller(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
      
      

    def __str__(self):
        return self.title
class Mystery(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
      
      

    def __str__(self):
        return self.title
class War(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
      
      

    def __str__(self):
        return self.title                        

class Adventure(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class History(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Foreign(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Horror(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Documentary(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Music(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class ScienceFiction(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class TVMovie(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Western(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)

    def __str__(self):
        return self.title

class Fantasy(models.Model):
    genres = models.CharField(max_length=300,blank = True)
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    rating = models.FloatField(default = 0,
          validators=[
               MaxValueValidator(5), MinValueValidator(0),
          ]
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    fantasy = models.ForeignKey(Fantasy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.fantasy.title + "(" + str(self.rating) + ")"


class MovieList(models.Model):
    genres = CharField(max_length=300, blank = 'True')
    id= models.CharField(max_length = 300,primary_key = 'True')
    original_title= models.TextField(blank = True)
    title= models.TextField(blank =True)
    rating = models.FloatField(default = 0,
        validators=[
            MaxValueValidator(5), MinValueValidator(0),
          ]
    )

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.movie.title + "(" + str(self.rating) + ")"




class PopularMovies(models.Model):
    genres = models.CharField(max_length = 300)
    title = models.CharField(max_length = 200)
    
    id= models.CharField(max_length = 300,primary_key = 'True')



    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    
    description = models.TextField()

    def __str__(self):
        return self.name









