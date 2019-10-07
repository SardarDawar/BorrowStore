from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    tracking_id = models.CharField(max_length=100, )
    slug = models.SlugField(max_length=100, )
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    date_acquired = models.DateTimeField()
    date_remove = models.DateTimeField(blank=True,null=True)
    disposal_note = models.TextField(blank=True)
    active_item = models.BooleanField(default=True)
    image = models.ImageField( blank=True)
    
   
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

