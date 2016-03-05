# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

#from django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.enocoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

#from mine


# Create your models here.
@python_2_unicode_compatible
class User(AbstractUser):
    u'''
        
    '''
    name = models.CharField(_("用户名"), blank=True, max_len=255)
    
    def __str__(self):
        return self.username
        
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})