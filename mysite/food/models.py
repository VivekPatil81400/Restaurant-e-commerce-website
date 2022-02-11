from django.db import models

# Create your models here.
class Item(models.Model):


    def __str__(self):
        return self.Item_name

    Item_name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()
    Item_image = models.CharField(max_length=500,default='https://i.ebayimg.com/images/g/QloAAOSwejpfe1JN/s-l300.jpg')

