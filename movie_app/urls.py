from django.contrib import admin
from django.urls import path
from movie_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('signup/',views.signup,name="signup"),

    path('',views.home,name="home"),
    path('user_movie_list/<int:user_id>/', views.user_movie_list, name='user_movie_list'),
    path("addmovie/",views.addmovie,name="addmovie"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("search_by_title/",views.search_by_title,name="search_by_title"),
    path('rate/', views.rate_movie, name='rate_movie'),
    path('rate/success/', views.rate_movie_success, name='rate_movie_success'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('rate/', views.rate_movie, name='rate_movie'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_review/', views.add_review, name='add_review'),
    path('review_success/', views.review_success, name='review_success'),
    path('add_review/<int:movie_id>/', views.add_review, name='add_review'),
    path('show_reviews/<int:movie_id>/', views.show_reviews, name='show_reviews'),
    path('show_reviews/<int:movie_id>/', views.show_reviews, name='show_reviews'),
    path('show_reviews/<int:movie_id>/', views.show_reviews, name='show_reviews'),

    path('genre/<str:genre>/', views.genre_view, name='genre_view'),
    path('genre/<str:genre>/', views.genre_view, name='genre_view'),

    # path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # Add the URL pattern with the success parameter
    path('show_reviews/<int:movie_id>/', views.show_reviews, {'success': True}, name='show_reviews_success'),




]