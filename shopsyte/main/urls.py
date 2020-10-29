from django.urls import path,include
from . import views
 
                                                                                                            
urlpatterns = [
    path("index/", views.index),
    path('<int:game_id>/', views.details),
    path('search/', views.search),
    path('search/searching/', views.searching),
    path('<int:game_id>/comment/', views.comment ),
    path('<int:game_id>/comment/commenting/', views.commenting ),
    path('<int:game_id>/<int:comment_id>/upvote/', views.upvote),
    path('<int:game_id>/<int:comment_id>/downvote/', views.downvote),
    path('register/', views.register_page),
    path('registrate/', views.register),

    ]