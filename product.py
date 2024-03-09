import peewee
from main import database_manager


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


    def __str__(self) -> str:
        return f'ID: {self.id}\nProduct Name: {self.product_name}\nPrice: {self.product_price}'


    class Meta:
        database = database_manager.db
