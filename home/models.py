# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Recipes(models.Model):

    #__Recipes_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.TextField(max_length=255, null=True, blank=True)
    instructions = models.TextField(max_length=255, null=True, blank=True)

    #__Recipes_FIELDS__END

    class Meta:
        verbose_name        = _("Recipes")
        verbose_name_plural = _("Recipes")


class Blogs(models.Model):

    #__Blogs_FIELDS__
    blog_content = models.CharField(max_length=255, null=True, blank=True)

    #__Blogs_FIELDS__END

    class Meta:
        verbose_name        = _("Blogs")
        verbose_name_plural = _("Blogs")



#__MODELS__END
