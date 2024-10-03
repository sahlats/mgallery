"""
URL configuration for mgallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("create/",views.MovieCreateView.as_view(),name='movie_create'),
    path("list/",views.MovieListView.as_view(),name="movie_list"),
    path('detail/<int:pk>',views.MovieDetailView.as_view(),name="movie_detail"),
    path('delete/<int:pk>/remove',views.MovieDeleteView.as_view(),name="movie-delete"),
    path('update/<int:pk>/change',views.MovieUpdateView.as_view(),name="movie-update")
]

