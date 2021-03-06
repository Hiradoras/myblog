from email import header
from random import choice
from django import forms
from .models import Post, Category, Comment

# You can hardcode it like that but it's not dynamic
# choices = [('coding', 'coding'), ("sports","sports"), ('entertainment','entertainment')]

# This is better choice. It's get categories directly from database.
choices = Category.objects.all().values_list('name','name')

choice_list = [x for x in choices]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','author','body', 'snippet','category', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            'category' : forms.Select(choices = choice_list,  attrs={'class' : 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet', 'category', 'header_image')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
            #'author' : forms.Select(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            'category' : forms.Select(choices = choice_list,  attrs={'class' : 'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

