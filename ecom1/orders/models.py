from django.db import models
from shop.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class staff_contractor_company(models.Model):#bana do
    user                      =     models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    company_name                     =     models.CharField(max_length=100)
    company_description              =     models.CharField(max_length=100)
    email_address                    =     models.EmailField()
    location                         =     models.TextField()
    work_phone                       =     models.CharField(max_length=1000)
    mobile_phone                     =     models.CharField(max_length=1000)
    emergency_phone                  =     models.CharField(max_length=1000)
    emergency_contact                =     models.CharField(max_length=1000)
    emergency_contact_note           =     models.TextField()
    fax_number                       =     models.CharField(max_length=1000)
    addressline_1                    =     models.CharField(max_length=100)
    addressline_2                    =     models.CharField(max_length=100)
    city                             =     models.CharField(max_length=25)
    province_state                   =     models.CharField(max_length=25)
    postal_code                      =     models.CharField(max_length=25)
    country_region                   =     models.CharField(max_length=25)
    website                          =     models.URLField()
    
    class Meta:
        verbose_name_plural='staff_contractor_company'
    def __str__(self):
        return self.company_name


class assset_tracker_activity(models.Model):
    asset_tracking_id               =      models.ForeignKey(Product,on_delete = models.CASCADE , null = True)
    user                     =      models.CharField(max_length=100,null=True)
    note                            =      models.CharField(max_length=100,null=True)
    location_being_moved_to         =      models.TextField(blank=True)
    move_date                       =      models.DateField(blank=True)
    due_for_pickup                  =      models.DateField(blank=True)                    
    item_status                     =      models.CharField(max_length=100,null=True)
    detailed_note                   =      models.TextField(null=True)  
    returned                        =      models.BooleanField(default=False)
    class Meta:
        verbose_name_plural='assset_tracker_activity'
    def __str__(self):
        return self.user
   

class Location(models.Model):
    product = models.ForeignKey(assset_tracker_activity,on_delete=models.CASCADE)
    location = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural='Location'
    def __str__(self):
        return self.locatio

class history_order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    item = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item
