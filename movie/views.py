from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie,MovieLink

#class ModelNameList(ListView):
   # model=ModelName
 #   context_object_name=

class HomeView(ListView):
    model = Movie
    template_name='movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['top_rated']=Movie.objects.filter(status='TR')
        context['most_watched']=Movie.objects.filter(status='MW')
        context['recently_added']=Movie.objects.filter(status='RA')
        return context

class MovieList(ListView):
    model = Movie
    paginate_by=1


class MovieDetail(DetailView):
    model = Movie
    # template_name = ".html"


    #getting the object
    def get_object(self):
        object=super(MovieDetail,self).get_object()
        object.views_count+=1
        object.save()
        return object
    
    #for getting links for the object
    def get_context_data(self, **kwargs):
        context=super(MovieDetail,self).get_context_data(**kwargs)
        context['links']=MovieLink.objects.filter(movie=self.get_object())
        context['related_movies']=Movie.objects.filter(category=self.get_object().category).order_by('created')[0:6]
        return context


class MovieCategory(ListView):
    model = Movie
    def get_queryset(self):
         self.category=self.kwargs['category']
         movies=Movie.objects.filter(category=self.category)
         self.cat_value=Movie.get_categories(self.category)
        #  if len(movies)!=0:
        #     self.cat_value=movies[0].get_category_display()#get value for category choice
         return movies

    def get_context_data(self, **kwargs):
        context = super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']=self.cat_value
        return context

class MovieLanguage(ListView):
    model = Movie
    def get_queryset(self):
         self.language=self.kwargs['lang']
         movies=Movie.objects.filter(language=self.language)
        #  mov_obj=Movie()
         self.lang_value=Movie.get_languages(self.language)
        #  if len(movies)!=0:
        #     self.lang_value=movies[0].get_language_display()#get value for category choice
         return movies

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language']=self.lang_value
        return context
        
class MovieSearch(ListView):
    model = Movie
    def get_queryset(self):
        query=self.request.GET.get('query')
        if query:
            movies=self.model.objects.filter(title__icontains=query)
        else:
            movies=self.model.objects.none()
        self.query_value=query
        print(query)
        return movies 

    def get_context_data(self, **kwargs):
        context = super(MovieSearch,self).get_context_data(**kwargs)
        context['query']=self.query_value
        return context
     
    
class MovieYear(YearArchiveView):
    queryset=Movie.objects.all()
    date_field='year_of_production'
    make_object_list = True
    allow_future = True 


 