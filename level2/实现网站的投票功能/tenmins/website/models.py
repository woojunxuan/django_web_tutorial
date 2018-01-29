from django.db import models
from faker import Factory

class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# f = open('D:\\codes\\git\\django_web_tutorial\\level2\\用django分页器实现文章分页\\tenmins\\website\\web_url.txt')
# fake = Factory.create()
# for url in f.readlines():
#     print('{}--'.format(url.rstrip('\n')))
#     v = Video(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#         url_image=url.rstrip('\n'),
#         editors_choice=fake.pybool()
#         )
#     v.save()
