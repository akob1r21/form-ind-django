from django.db import models
from django.utils.text import slugify
from .managers import ProductManager, AllProductManager


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    



class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            first_slug = slugify(self.title)
            counter = 1 # red-hat-3

            while Product.objects.filter(slug=first_slug).exists():
                counter+=1
                first_slug = f'{first_slug}-{counter}'

            self.slug = first_slug
            
            
        return super().save(*args, **kwargs)
    
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()



    class Meta:
        permissions = [
            ('can_sell_products', 'Can Sell Products')
        ]

    objects = ProductManager()
    all_objects = AllProductManager()

    

    
    