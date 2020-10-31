from django.urls import path,include
from . import views
 
                                                                                                            
urlpatterns = [
    path("home/", views.index),
    path('<str:game_title>/', views.details),
    path('home/search/', views.search),
    path('searching/', views.searching),
    path('<int:game_id>/comment/', views.comment ),
    path('<int:game_id>/comment/commenting/', views.commenting ),
    path('<int:game_id>/<int:comment_id>/upvote/', views.upvote),
    path('<int:game_id>/<int:comment_id>/downvote/', views.downvote),
    path('register/', views.register_page),
    path('registrate/', views.register),

    ]