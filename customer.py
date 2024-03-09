import peewee
from constants import CURRENT_YEAR
from product import Product
import jdatetime
from main import database_manager


class Customer(peewee.Model):
    '''Customers class'''
    first_name = peewee.CharField(
        max_length=50,
        null=False,
        verbose_name='First Name'
    )
    last_name = peewee.CharField(
        max_length=50,
        null=False,
        verbose_name='Last Name'
    )
    birthday = peewee.IntegerField(
        null=False,
        verbose_name='Birthday'
    )
    number = peewee.CharField(
        max_length=20,
        null=False,
        verbose_name='Number'
    )


    @property
    def full_name(self) -> str:
        '''
        Concatinate first name and last name to create full name
        '''
        return f'{self.first_name} {self.last_name}'


    @property
    def age(self) -> int:
        '''
        Calculate customers age
        '''
        return CURRENT_YEAR - self.birthday


    def __str__(self) -> str:
        return (
            f'ID: {self.id}\nName: {self.full_name}\n'
            f'Age: {self.age}\nNumber: {self.number}'
        )


    def buy_product(self, product: Product, date: jdatetime.date) -> dict:
        '''Buy a product by a customer'''
        return {
            'Customer': self,
            'Product': product,
            'Date': date
        }


    class Meta:
        database = database_manager.db
