# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

#from django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils.enocoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

#import myself

u'''
参考文献：
1、AbstractBaseUser provides the core implementation of a User model, including hashed passwords and tokenized password resets
2、The documentation explains this fully. AbstractUser is a full User model, 
compete with fields, as an abstract class so that you can inherit from it and add your own profile fields and methods. 
AbstractBaseUser only contains the authentication functionality, but no actual fields: 
you have to supply them when you subclass.
'''
@python_2_unicode_compatible
class User(AbstractUser):
    u'''
        
    '''
    identifier = models.CharField(max_length=40, unique=True)
    name = models.CharField(_("用户名"), blank=True, max_len=255)
    
    def __str__(self):
        return self.username
        
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})