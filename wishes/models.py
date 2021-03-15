from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Wish(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishes'

    def __str__(self):
        if len(self.content) > 50:
            output = f'{self.content} ...'
        else:
            output = self.content
        return output

