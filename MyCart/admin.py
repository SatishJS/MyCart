from django.contrib import admin
from models import *

# Register your models here.
class MyCartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['bearer']}),
        (None, {'fields': ['total_amount']}),
        (None, {'fields': ['shared_user']}),
        (None, {'fields': ['share_amount']}),
        (None, {'fields': ['comments']}),
        (None, {'fields': ['transaction_id']}),
        (None, {'fields': ['transaction_status']}),
        (None, {'fields': ['approval_status']}),
        (None, {'fields': ['_created_date']}),
        (None, {'fields': ['_modified_date']}),
    ]
    readonly_fields = ('_created_date', '_modified_date')
    list_filter = ('bearer', 'shared_user', 'transaction_id', 'transaction_status', 'approval_status',)
    list_display = ('bearer', 'total_amount', 'shared_user', 'share_amount', 'comments',
                    'transaction_id', 'transaction_status', 'approval_status', '_created_date', '_modified_date')

admin.site.register(MyCart, MyCartAdmin)

# Register your models here.
class ProductCatalogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_id']}),
        (None, {'fields': ['product_name']}),
        (None, {'fields': ['product_category']}),
    ]
    list_filter = ('product_id', 'product_name', 'product_category',)
    list_display = ('product_id', 'product_name', 'product_category')

admin.site.register(ProductCatalog, ProductCatalogAdmin)

# Register your models here.
class UserCartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_id']}),
        (None, {'fields': ['user']}),
    ]
    list_filter = ('product_id', 'user',)
    list_display = ('product_id', 'user')

admin.site.register(UserCart, UserCartAdmin)
