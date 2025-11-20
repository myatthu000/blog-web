from django.db import models
from .models import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager


# Model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED) #return querySet will be executed

# Create your models here.
class Post(models.Model):

    class Status(models.TextChoices): #To save post as a draft until ready for publication
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)

    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish' #wont effect in db, so no migrations will occur.. publish date တစ်ရက်အတွင်း slug တစ်ခု
    )
    
    #manyToOne relationship
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #db_default=Now()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager() # The default manager
    published = PublishedManager() # My custom manager

    class Meta:
        ordering = ['-publish'] #order by reverse
        indexes = [
            models.Index(fields=['-publish']), #performance for query filtering or ordering results by this field
        ]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", 
            args=[
                # self.id
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                ]
            )
    
    tags = TaggableManager()
    
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}. '
    

