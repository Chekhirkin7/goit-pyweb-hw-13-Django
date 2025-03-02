from django.forms import CharField, TextInput, ChoiceField, Textarea, Select
from django import forms
from .models import Author, Quote


class QuoteForm(forms.Form):
    quote = CharField(label="Quote", widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your quote'}), required=True)
    author = forms.ChoiceField(
        label="Author",
        widget=Select(attrs={"class": "form-control"}),
        required=True
    )
    tags = CharField(label="Tags (comma-separated)", widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'tag1, tag2,tag3 ...'}), required=True)

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['author'].choices = [(str(author.id), author.fullname) for author in Author.objects]

    def clean_tags(self):
        tags_str = self.cleaned_data['tags']
        return [tag.strip() for tag in tags_str.split(',') if tag.strip()]

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


class AuthorForm(forms.Form):
    fullname = CharField(label="Fullname", widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Fullname'}), required=True)
    born_date = CharField(label="Born_date", widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Born date'}), required=True)
    born_location = CharField(label="Born_location", widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Born location'}), required=True)
    description = CharField(label="Description", widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}), required=True)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
