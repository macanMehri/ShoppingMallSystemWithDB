from customer import Customer
from product import Product
from shopping_mall import ShoppingMall
from database_manager import DatabaseManager
from constants import *
from local_settings import DATABASE
import jdatetime
import random


# Connect to database useing database_manager
database_manager = DatabaseManager(
    database_name=DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)

def create_random_customer(count: int) -> None:
    '''
    Creating random customers and add them to database
    As many as count variable
    '''
    for i in range(count):
        random_name = random.choice(FIRST_NAMES)
        random_last_name = random.choice(LAST_NAMES)
        random_birthday = random.randint(1300, CURRENT_YEAR)
        random_number = random.randint(1_000, 1_000_000_000_000)
        Customer.create(
            first_name=random_name,
            last_name=random_last_name,
            birthday=random_birthday,
            number=random_number
        )


def create_product() -> None:
    '''Creating products and add them to database'''
    for product in PRODUCTS:
        random_price = random.randint(100_000, 10_000_000)
        Product.create(
            product_name=product,
            product_price=random_price
        )


if __name__ == '__main__':
    try:
        # Create tables
        database_manager.create_tables(
            [Customer, Product, ShoppingMall]
        )
        print(MENU)
        order = int(input('Please enter a number to run the command: '))
        create_random_customer(3)
        create_product()
    except ValueError as error:
        print(error)
    finally:
        # Closing database connection.
        if database_manager.db:
            database_manager.db.close()
            print('Database connection is closed')
