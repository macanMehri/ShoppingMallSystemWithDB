import peewee
from customer import Customer
from product import Product
import jdatetime


class ShoppingMAll(peewee.Model):
    '''Shopping Mall Class'''

    bought_product = peewee.ForeignKeyField(
        model=Product,
        null=False,
        verbose_name='Bought Product'
    )

    customer = peewee.ForeignKeyField(
        model=Customer,
        null=False,
        verbose_name='Customer'
    )

    date = peewee.DateField(
        default=jdatetime.datetime.now().date()
    )
