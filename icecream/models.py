from django.db import models

# Attribute and data type explaination given in word doc.

class store(models.Model):
    name = models.CharField(max_length=200)               #string field
    store_location = models.CharField(max_length=200)     #String field
    email_id = models.EmailField()                        #email field

    def __str__(self):
        return f"{self.name} - {self.store_location}"   #showing name of store and location on list for better readability

class tub(models.Model):
    FLAVORS = [
        ('VANILLA', 'Vanilla'),
        ('CHOCOLATE', 'Chocolate'),
        ('STRAWBERRY', 'Strawberry'),
        ('MATCHA', 'Matcha'),
        ('COFFEE', 'Coffee'),
    ]

    store = models.ForeignKey(store, on_delete=models.CASCADE, related_name='tubs')
    flavor = models.CharField(max_length=15, choices=FLAVORS)          # for choices dropdown containing flaovors. Django documentation
    size = models.DecimalField(max_digits=7, decimal_places=2)
    is_vegan = models.BooleanField()
    is_gluten_free = models.BooleanField()

    def __str__(self):
        return f"{self.flavor} - {self.size}L"
