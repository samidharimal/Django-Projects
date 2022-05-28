from django.contrib import admin
from.models import *
from import_export.admin import ImportExportModelAdmin

@ admin.register(MovieList,Animation,Comedy,Family,Romance,Crime,Drama,Action,Thriller,Mystery,War,Adventure,History,Foreign,Horror,Documentary,Music,ScienceFiction,
TVMovie,Western,Fantasy,PopularMovies,MovieGenre, Review,MovieReview,Contact)

class ViewAdmin(ImportExportModelAdmin):
    pass