from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Smartphone(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Tablet(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
##############################
class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    

    def __str__(self):
        return self.name
