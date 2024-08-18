from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Movie
from .models import Review
class movieform(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('added_by',)  # Exclude 'added_by' field as it will be set automatically in the view
        labels = {
            'title': 'Movie Title',
            'genres': 'Genres',
            'year': 'Year',
            'image': 'Image',
            'movieduration': 'Duration',
            'description': 'Description',
            'actors': 'Actors',
            'link': 'Link',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'movieduration': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'actors': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }



from django import forms
from .models import Movie

class AddMovieForm(forms.ModelForm):
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror','Horror'),
        ('romantic','Romantic'),
        # Add more genre choices as needed
    )

    genres = forms.ChoiceField(choices=GENRE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Movie
        exclude = ('added_by',)  # Exclude 'added_by' field from the form
        labels = {
            'title': 'Movie Title',
            'year': 'Year',
            'image': 'Image',
            'movieduration': 'Duration',
            'description': 'Description',
            'actors': 'Actors',
            'link': 'Link',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'movieduration': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'actors': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email Address'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class DeleteMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ['username', 'password']



from django import forms
from .models import Movie

class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genres', 'year', 'image', 'movieduration', 'description', 'actors', 'link']




class ReviewForm(forms.ModelForm):
            class Meta:
                model = Review
                fields = ['name','rating','review_text']


from django import forms

class GenreForm(forms.Form):
    genre = forms.CharField(
        label='Genre',
        widget=forms.Select(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('drama', 'Drama')]),
        required=True,
        help_text="Please select a genre"
    )

    # Optional: Add custom validation if needed
    # def clean_genre(self):
    #     genre = self.cleaned_data.get('genre')
    #     # Add validation logic here
    #     return genre