from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug +'-'+ str(int(time()))

class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.FileField(blank=True, null=True, upload_to='media')
    price = models.CharField(max_length=20)


    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    def delete_url(self):
        return reverse('product_delete_url',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
