from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

CATEGORY_CHOICES=(
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE'),
)
LANGUAGE_CHOICES=(
    ('EN','ENGLISH'),
    ('GR','GERMAN'),

)
STATUS_CHOICES=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED')
)


class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='movies')
    banner=models.ImageField(upload_to='movies/banner')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    cast=models.CharField(max_length=100)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=2)
    status=models.CharField(choices=STATUS_CHOICES,max_length=2)
    year_of_production=models.DateField()
    views_count=models.IntegerField(default=0)
    trailer_link=models.URLField()
    created=models.DateTimeField(default=timezone.now)


    slug=models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Movie,self).save(*args,**kwargs)


    #For title to be shown in django admin page
    def __str__(self):
        return self.title
    def get_categories(cat):
        return dict(CATEGORY_CHOICES).get(cat)
    def get_languages(lang):
        return dict(LANGUAGE_CHOICES).get(lang)


LINK_CHOICES=(
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK'),
)

class MovieLink(models.Model):
    #on delete cascade, if we delete movie we will delete the watch links as well
    movie=models.ForeignKey('Movie', related_name='movie_watch_link', on_delete=models.CASCADE)
    type=models.CharField(choices=LINK_CHOICES, max_length=1)
    link=models.URLField()
    def __str__(self):
        return str(self.movie)+" "+self.get_type_display()#to join movie name+link type choice value
    




