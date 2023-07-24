from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE ,max_length=20)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE ,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.content}] {self.content} :: {self.writer}'
    
    def get_absolute_url(self):
        return f'/blog/{self.post.pk}/#comment-{self.pk}'
    
    class Meta:
        ordering = ['-id']
    


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode = True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'
    
    class Meta:
        verbose_name_plural = 'Categories'
