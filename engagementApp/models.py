from django.conf import settings
from django.db import models
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField(
        upload_to='photos', null=True, max_length=255)
    category = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    liked = models.BooleanField(default=True)
    owner = models.ForeignKey(
        'auth.User', related_name='articles', on_delete=models.CASCADE, null=True)
    # highlighted = models.TextField(null = True)
     
    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTMLz
    #     representation of the code snippet.
    #     """
    #     # lexer= get_lexer_by_name(self.language)
    #     # linenos = 'table' if self.linenos else False
    #     options = {'title':self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Articles, self).save(*args, **kwargs)

    
