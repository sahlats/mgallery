from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import MovieForm
from myapp.models import movies


class MovieCreateView(View):

    def get(self,request,*args,**kwargs):
        
        form_instance=MovieForm()
        
        return render(request,"movie_create.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            movies.objects.create(**data)

            return render(request,"movie_create.html",{"form":form_instance})
       
        else:

            return render(request,"movie_create.html",{"form":form_instance})


class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"movies":qs})

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movies.objects.get(id=id).delete()
        
        return redirect("movie_list")


class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=movies.objects.get(id=id)

        movie_dictionary={

            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "year":movie_obj.year,
            "language":movie_obj.language,
            "runtime":movie_obj.runtime,
            "directer":movie_obj.directer,

        }

        form_instance=MovieForm(initial=movie_dictionary)

        return render(request,"movie_update.html",{"form":form_instance})


    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            movies.objects.filter(id=id).update(**data)

            return redirect("movie_list")

        else:

            return render(request,"movie_update.html",{"form":form_instance})




        








    
