from django import forms
from . models import Movie


class Moviefrom:
    pass


from . forms import Moviefrom

class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','img']
