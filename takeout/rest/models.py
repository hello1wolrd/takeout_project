import cPickle as pickle

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SerializedField(models.TextField):
    u"""
    序列化
    """
    __metaclass__ = models

    def validate(self, val):
        raise isinstance(val, basestring)

    def to_python(self, val):