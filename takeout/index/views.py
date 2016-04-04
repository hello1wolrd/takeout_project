# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


#django
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

#mysetting
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class IndexView(TemplateView):
    template_name = "index/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class LoginView(TemplateView):
    template_name = "index/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def post(self, request):
        print "login"
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            reverse_url = reverse('index:register')
            return HttpResponseRedirect(reverse_url)

        user = authenticate(username=username, password=password)
        if user is not None:
            reverse_url = reverse('index:index')
            return HttpResponseRedirect(reverse_url)


class RegisterView(TemplateView):
    template_name = "index/register.html"

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context

    def post(self, request):
        print "register"
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print "create user"
            #create 
            user = User.objects.create_user(username=username, password=password)
            user.save()
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            reverse_url = reverse('index:index')
            return HttpResponseRedirect(reverse_url)

        print "chongfu "
        return render(request, 'index/register.html', {'user_err': '重复的用户名'})


def logout(request):
    
    return HttpResponse("logout")    








