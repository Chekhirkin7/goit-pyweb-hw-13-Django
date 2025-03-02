from django.shortcuts import render, redirect
from django.views import View
from .models import Quote, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuoteForm, AuthorForm


class HomeViews(View):
    template_name = 'quotes/index.html'

    def get(self, request):
        quotes = Quote.objects.all()
        return render(request, self.template_name, {'quotes': quotes})


class AuthorDetailView(View):
    template_name = 'quotes/author_detail.html'

    def get(self, request, fullname):
        author = Author.objects.get(fullname=fullname)
        return render(request, self.template_name, {'author': author})


class TagDetailView(LoginRequiredMixin, View):
    login_url = '/app_auth/signin/'
    template_name = 'quotes/find_tag.html'

    def get(self, request, tag):
        quotes = Quote.objects.filter(tags=tag)
        return render(request, self.template_name, {'quotes': quotes, 'tag': tag})


class AddQuoteView(LoginRequiredMixin, View):
    login_url = '/app_auth/signin/'
    template_name = 'quotes/add-quote.html'
    form_class = QuoteForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['quote']
            author = form.cleaned_data['author']
            tags = form.cleaned_data['tags']

            new_quote = Quote(quote=quote_text, author=author, tags=tags)
            new_quote.save()
            return redirect('quotes:index')
        return render(request, self.template_name, {'form': form})


class AddAuthorView(LoginRequiredMixin, View):
    login_url = '/app_auth/signin/'
    template_name = 'quotes/add-author.html'
    form_class = AuthorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            born_date = form.cleaned_data['born_date']
            born_location = form.cleaned_data['born_location']
            description = form.cleaned_data['description']

            new_author = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
            new_author.save()
            return redirect('quotes:index')
        return render(request, self.template_name, {'form': form})
