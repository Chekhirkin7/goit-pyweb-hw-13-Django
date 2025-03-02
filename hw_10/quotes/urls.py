from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.HomeViews.as_view(), name='index'),
    path('authors/<str:fullname>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path("tag/<str:tag>/", views.TagDetailView.as_view(), name = 'find_tag'),
    path('add-quote/', views.AddQuoteView.as_view(), name='add-quote'),
    path('add-author/', views.AddAuthorView.as_view(), name='add-author')
]
