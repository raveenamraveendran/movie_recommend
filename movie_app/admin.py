from django.contrib import admin
from .models import Movie,Review

# Register your models here.
@admin.register(Movie)
class movieAdmin(admin.ModelAdmin):
    list_display=('id','title','genres','year','image','movieduration','description','actors','link','added_by')

@admin.register(Review)
class ratingAdmin(admin.ModelAdmin):
    list_display=('name','movie','rating','review_text')
