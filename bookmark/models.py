from django.db import models

# Create your models here.

class Bookmark(models.Model):
    # pk없으면 자동으로 증가되는 필드가 만들어진다.
    title = models.CharField('TITLE',max_length=100,blank=True)
    url = models.URLField('URL', null=True )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title