from django.shortcuts import render
from .models import Game, Comment
from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from .forms import CommentForm,SearchForm,LoginForm,EnterForm,ChoiceForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    games = Game.objects.filter()
    context = {"games":games}
    return render(request,"index.html",context)

def details(request, game_id):

    value = Game.objects.get(id = game_id)
    game = get_object_or_404(Game, pk=game_id)
    c_list = Comment.objects.filter(game = value)
    context = {'game': game,'commentarys':c_list}
    return render(request, 'details.html', context)


def search(request):

        _SearchForm = SearchForm
        context = {"search_form":_SearchForm}
        return render(request, 'search.html',context)


def searching(request):

        if request.method == "POST":
            value = request.POST.get("text")
            game = Game.objects.get(title = value)
            link = '//127.0.0.1:8000/' + str(game.id)
            return redirect(link)

@login_required
def comment(request, game_id):

        _CommentForm = CommentForm()
        return render(request, 'comment.html',{'form':_CommentForm})

@login_required
def commenting(request, game_id):

        if request.method == "POST":
            text = request.POST.get("text")
            game = Game.objects.get(id = game_id)
            comment = Comment(texts= text,game = game, user = request.user)
            comment.save()
            link = '//127.0.0.1:8000/' + str(game_id)
            return redirect(link)

@login_required
def upvote(request, comment_id, game_id):

    comment = Comment.objects.get(id = comment_id)
    comment.upvotes += 1
    comment.save()
    link = '//127.0.0.1:8000/'+ str(game_id)
    return redirect(link)

@login_required
def downvote(request, comment_id, game_id):

    comment = Comment.objects.get(id = comment_id)
    comment.downvotes += 1
    comment.save()
    link = '//127.0.0.1:8000/'+ str(game_id)
    return redirect(link)

def register_page(request):

    _LoginForm = LoginForm()
    context = {'login_form':_LoginForm}
    return render(request, 'register.html', context)

def register(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(name, email, password)
        context = {'user': user}
        return redirect('//127.0.0.1:8000/accounts/login/')
