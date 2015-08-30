import datetime
import requests, json
from models import *
from django.db.models import Q
from django.contrib.auth.models import User

from django.db.models import Sum
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/mycart/accounts/home')
    else:
        return HttpResponseRedirect('/mycart/accounts/invalid')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


@login_required(login_url='/mycart/accounts/login/')
def home(request):
    c = {}
    c.update({'full_name': request.user.username,
              'email': request.user.email,
              'FRIENDS': User.objects.all()})
    c.update(csrf(request))

    return render_to_response('home.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def invalid_login(request):
    return render_to_response('invalid_login.html')


@login_required(login_url='/mycart/accounts/login/')
def get_catalog(request):

    user_cart = UserCart.objects.filter(user=request.user.username)
    p_catalog  = ProductCatalog.objects.exclude(product_id__in=user_cart.values_list('product_id', flat=True))
    p_category = p_catalog.values_list('product_category', flat=True).distinct()

    c = {}
    c.update({'full_name': request.user.username})
    c.update({'v_category': p_category})
    c.update({'v_catalog': p_catalog})

    c.update(csrf(request))
    return render_to_response('catalog.html', c)

@login_required(login_url='/mycart/accounts/login/')
def my_cart(request):

    user_cart = UserCart.objects.filter(user=request.user.username)
    p_catalog  = ProductCatalog.objects.filter(product_id__in=user_cart.values_list('product_id', flat=True))

    p_category = p_catalog.values_list('product_category', flat=True).distinct()

    c = {}
    c.update({'full_name': request.user.username})
    c.update({'v_category': p_category})
    c.update({'v_catalog': p_catalog})
    c.update(csrf(request))

    return render_to_response('mycart.html', c)

@login_required(login_url='/mycart/accounts/login/')
def add_to_cart(request):
    user = User.objects.get(username=request.user.username).username
    prd_id = request.POST.get('prd-id')

    try:
        uc = UserCart()
        uc.product_id = prd_id
        uc.user = user
        uc.save()

    except IntegrityError as e:
        print e.message

    user_cart = UserCart.objects.filter(user=request.user.username)
    p_catalog  = ProductCatalog.objects.exclude(product_id__in=user_cart.values_list('product_id', flat=True))
    p_category = p_catalog.values_list('product_category', flat=True).distinct()

    c = {}
    c.update({'full_name': request.user.username})
    c.update({'v_category': p_category})
    c.update({'v_catalog': p_catalog})

    c.update(csrf(request))
    return render_to_response('catalog.html', c)

@login_required(login_url='/mycart/accounts/login/')
def remove_from_cart(request):
    user = User.objects.get(username=request.user.username).username
    prd_id = request.POST.get('prd-id')

    try:
        UserCart.objects.filter(user=user, product_id=prd_id).delete()
    except IntegrityError as e:
        print e.message

    user_cart = UserCart.objects.filter(user=request.user.username)
    p_catalog  = ProductCatalog.objects.filter(product_id__in=user_cart.values_list('product_id', flat=True))

    p_category = p_catalog.values_list('product_category', flat=True).distinct()

    c = {}
    c.update({'full_name': request.user.username})
    c.update({'v_category': p_category})
    c.update({'v_catalog': p_catalog})

    c.update(csrf(request))

    return render_to_response('mycart.html', c)