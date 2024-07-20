from django.db import models
from accounts.models import User

class Post(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    prefecture = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'posts'
        ordering = ["-create_at"]

class Comment(models.Model):
    content = models.TextField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return self.create_at
    
    class Meta:
        db_table = 'comments'
        ordering = ["-create_at"]