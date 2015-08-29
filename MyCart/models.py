from django.db import models
# Create your models here.


class MyCart(models.Model):

    bearer = models.CharField(max_length=15, blank=False)
    shared_user = models.CharField(max_length=15, blank=False)

    total_amount = models.IntegerField(null=False)
    share_amount = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    comments = models.CharField(max_length=20, blank=True)
    transaction_id = models.CharField(max_length=15)
    transaction_status = models.CharField(max_length=15)
    approval_status = models.CharField(max_length=15)

    _created_date = models.DateTimeField(auto_now_add=True)
    _modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(' | ' + self.bearer + ' | ' + str(self.total_amount) + ' | ' + self.shared_user + ' | ' + str(self.share_amount) + ' | ')

class ProductCatalog(models.Model):

    product_id = models.CharField(max_length=25, blank=False)
    product_name = models.CharField(max_length=255, blank=False)
    product_category = models.CharField(max_length=50, blank=False)


class UserCart(models.Model):

    product_id = models.CharField(max_length=25, blank=False)
    user = models.CharField(max_length=25, blank=False)
