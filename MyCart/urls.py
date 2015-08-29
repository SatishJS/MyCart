from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^$', 'MyCart.views.login'),

   url(r'^accounts/auth/$', 'MyCart.views.auth_view'),
   url(r'^accounts/login/$', 'MyCart.views.login'),
   url(r'^accounts/home/$', 'MyCart.views.home'),

   url(r'^get/catalog/$', 'MyCart.views.get_catalog'),
   url(r'^addtocart/$', 'MyCart.views.add_to_cart'),
   url(r'^remove-from-cart/$', 'MyCart.views.remove_from_cart'),

   url(r'^get/mycart/$', 'MyCart.views.my_cart'),
   url(r'^accounts/logout/$', 'MyCart.views.logout'),
   url(r'^accounts/invalid/$', 'MyCart.views.invalid_login'),


   )