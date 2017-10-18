from django.db import models
from django.conf import settings


# Create your models here.


class OAuthUser(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', blank=True, null=True)
    openid = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    picture = models.CharField(max_length=350, blank=True, null=True)
    type = models.CharField(blank=False, null=False, max_length=50)
    email = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name
