import peewee


class Product(peewee.Model):
    '''Product class'''
    product_name = peewee.CharField(
        max_length=50,
        null=False,
        verbose_name='Product Name'
    )
    product_price = peewee.FloatField(
        null=False,
        verbose_name='Product Price'
    )
