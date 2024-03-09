import peewee
from customer import Customer
from product import Product
import jdatetime


class ShoppingMall(peewee.Model):
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


    def __str__(self) -> str:
        return (
            f'Purchased ID: {self.id}\n'
            f'Customer: {self.customer}\n'
            f'Product: {self.bought_product}\n'
            f'Date: {self.date}'
        )
