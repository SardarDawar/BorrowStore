from django.db import models
from django.contrib.auth.models import User
from random import randint
from orders.models import staff_contractor_company

class infor(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , null = True)
    passwordkey = models.CharField(max_length = 25 , null = True)

    def __str__(self):
        return (str(self.user))

class staff_contractor(models.Model):
    staff_name = models.CharField(null = True,max_length=200,blank=True)
    staff_contractor_company_id = models.ManyToManyField(staff_contractor_company)
    phone_password = models.CharField(null=True,max_length=25,blank=True)
    job_title = models.CharField(null=True,max_length=100,blank=True)
    work_phone = models.CharField(max_length=100,blank=True)
    home_phone = models.CharField(max_length=100,blank=True)
    mobile_phone = models.CharField(max_length=100,blank=True)
    fax_number = models.CharField(max_length=100,blank=True)
    address_line_1 = models.CharField(max_length=100,blank=True)
    address_line_2 = models.CharField(max_length=100,blank=True)
    city = models.CharField(null=True,max_length=30,blank=True)
    province_state = models.CharField(blank=True,max_length=30)
    postal_code_ZIP = models.CharField(blank=True,max_length=20)
    country_region = models.CharField(blank=True,max_length=30)
    web_page = models.URLField(blank=True)
    notes = models.TextField(blank=True,max_length=1000)
    archive = models.BooleanField(blank=True,default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user)