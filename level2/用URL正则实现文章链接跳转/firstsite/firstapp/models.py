from django.db import models

# Create your models here
class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

class Aritcle(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICES = (
        # 前一个是对应的值,后一个是对应的名字也就是在django admin后台所看见的值
        ('tech', 'Tech'),
        ('life', 'Life'),
    )
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Aritcle, related_name='under_comments', null=True,
                                  blank=True, on_delete=models.CASCADE)
    best_comment = models.BooleanField(default=False)
    comment_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment
