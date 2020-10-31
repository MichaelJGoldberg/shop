from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(max_length=400)

class SearchForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={"class":"searchform","autocomplete":"off"}),max_length=100)

class LoginForm(forms.Form): 
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    password = forms.IntegerField()
    email = forms.EmailField()

class EnterForm(forms.Form): 
    name = forms.CharField(max_length=100)
    password = forms.IntegerField()

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(max_length=100)