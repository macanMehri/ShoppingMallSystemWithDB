from shopping_mall import ShoppingMall
from constants import FIRST_NAMES, LAST_NAMES, PRODUCTS, CURRENT_YEAR, MENU
from database_manager import database_manager
from product import Product
from customer import Customer
import jdatetime
import random



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


def create_customer() -> None:
    '''Create a customer and add to mall customers list'''
    try:
        while True:
            first_name = input('Please enter your first name: ').capitalize()
            if not first_name.isdigit() and len(first_name) > 2:
                break
            print('This name is not allowed! Please try again.')

        while True:
            last_name = input('Please enter your last name: ').capitalize()
            if not last_name.isdigit() and len(last_name) > 2:
                break
            print('This last name is not allowed! Please try again.')

        while True:
            birth_year = int(input('Please enter your birthdate year: '))
            if 1300 < birth_year < CURRENT_YEAR:
                break
            print('Entery is not correct! Please try again.')

        while True:
            number = input('Please enter your number: ')
            if number.isdigit() and len(number) > 3:
                break
            print('This number is not allowed! Please try again.')

        Customer.create(
            first_name=first_name,
            last_name=last_name,
            birthday=birth_year,
            number=number
        )
    except Exception as error:
        print('ERROR:', error)
    else:
        print('New customer is added.')


def create_random_product() -> None:
    '''Creating products and add them to database'''
    for product in PRODUCTS:
        random_price = random.randint(100_000, 10_000_000)
        Product.create(
            product_name=product,
            product_price=random_price
        )


def create_product() -> None:
    '''This function creates a product and add to database'''
    try:
        while True:
            product_name = input('Please enter your product name: ')
            if not product_name.isdigit() and len(product_name) > 2:
                break
            print('This name is not allowed! Please try again.')
        while True:
            product_price = float(input('Please enter your product price: '))
            if product_price > 0:
                break
            print('This value is not allowed for price! Please try again.')
 
        Product.create(
            product_name=product_name,
            product_price=product_price
        )
    except ValueError as error:
        print('ERROR:', error)
    else:
        print('New product is added.')


if __name__ == '__main__':
    try:
        # Create tables
        database_manager.create_tables(
            [Customer, Product, ShoppingMall]
        )
        while True:
            print(MENU)
            order = int(input('Please enter a number to run the command: '))
            match order:
                case 0:
                    break
                case 1:
                    # Add new customer
                    create_customer()
                case 2:
                    # Add new product
                    create_product()
                    pass
                case 3:
                    # A customer buy a product
                    pass
            #create_random_customer(count=3)

    except ValueError as error:
        print(error)
    finally:
        # Closing database connection.
        if database_manager.db:
            database_manager.db.close()
            print('Database connection is closed')
