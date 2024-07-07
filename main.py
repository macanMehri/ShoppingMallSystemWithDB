from shopping_mall import ShoppingMall
from constants import FIRST_NAMES, LAST_NAMES, PRODUCTS, CURRENT_YEAR, MENU
from database_manager import database_manager
from product import Product
from customer import Customer
import matplotlib.pyplot as plt
import matplotlib.pyplot
from argparse import ArgumentParser
import jdatetime
import random
import sys


def create_random_customer(count: int) -> None:
    """
    Creating random customers and add them to database
    As many as count variable
    """
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
    """Create a customer and add to mall customers list"""
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
    """Creating products and add them to database"""
    for product in PRODUCTS:
        random_price = random.randint(100_000, 10_000_000)
        Product.create(
            product_name=product,
            product_price=random_price
        )


def create_product() -> None:
    """This function creates a product and add to database"""
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


def find_customer_by_id(customer_id: int):
    """Find customer by customers id"""
    return Customer.select().where(Customer.id == customer_id)


def find_product_by_id(product_id: int):
    """Find product by products name"""
    return Product.select().where(Product.id == product_id)


def find_product_by_name(product_name: str):
    """Find product by products name"""
    return Product.select().where(Product.product_name==product_name)


def show_all_customers():
    """Print all customers in database"""
    customers = Customer.select()
    for customer in customers:
        print(customer)
        print('-'*20)


def show_all_products():
    """Print all products in database"""
    products = Product.select()
    for product in products:
        print(product)
        print('-'*20)


def customer_exist(customer_id: int) -> bool:
    """Check if customer exists in database or not"""
    temp = Customer.select().where(Customer.id == customer_id)
    if temp:
        return True
    return False


def product_exist(product_id: int) -> bool:
    """Check if product exists in database or not"""
    temp = Product.select().where(Product.id == product_id)
    if temp:
        return True
    return False


def customer_buy_product(customer: int, product: int):
    """A customer buys a product in a time"""
    while True:
        time = input('Do you want to manualy enter date?(Y/N): ')
        if time == 'Y' or time == 'N':
            break
        print('Sorry I cannot understand your request! Please try again.')
    if time == 'N':
        year = jdatetime.datetime.now().year
        month = jdatetime.datetime.now().month
        day = jdatetime.datetime.now().day
    else:
        while True:
            year = int(input('Please enter year: '))
            if year <= CURRENT_YEAR:
                break
            print('Year is not allowed! Please try again.')

        while True:
            month = int(input('Please enter month: '))
            if 0 < month <= 12:
                break
            print('Month is not allowed! Please try again.')

        while True:
            day = int(input('Please enter day: '))
            if 0 < day <= 31:
                break
            print('Day is not allowed! Please try again.')

    ShoppingMall.create(
        customer=customer,
        bought_product=product,
        date=f'{year}-{month}-{day}'
    )


def sales_of_month(month: int) -> int:
    """Calculate total number of sales in a month"""
    count = 0
    purchases = make_list_of_purchases()
    for purchase in purchases:
        if purchase['Date'].month == month and purchase['Date'].year == CURRENT_YEAR:
            count += 1
    return count


def sale_of_year() -> list:
    """
    Each index in list shows number of month
    And in will calculate total sales of each month in this year
    """
    sales = list()
    for month in range(12):
        sales.append(sales_of_month(month=month+1))
    return sales


def earning_of_month(month: int) -> float:
    """Calculates total earnings of a month"""
    earning = 0
    purchases = make_list_of_purchases()
    for purchase in purchases:
        if purchase['Date'].month == month and purchase['Date'].year == CURRENT_YEAR:
            earning += purchase['Product'].product_price
    return earning


def earning_of_year() -> list:
    """
    Each index in list shows number of month
    And in will calculate total earnings of each month in this year
    """
    earnings = list()
    for month in range(12):
        earnings.append(earning_of_month(month=month+1))
    return earnings


def make_list_of_purchases() -> list:
    """
    Create a list of dictionaries of shoppingmall table
    """
    purchases = list(ShoppingMall.select())

    result = list()
    for purchase in purchases:
        # Customers and products are list of theyr ids. So we need to find the object
        product = find_product_by_id(product_id=purchase.bought_product)
        customer = find_customer_by_id(customer_id=purchase.customer)
        temp = {
            'Product': product[0],
            'Customer': customer[0],
            'Date': purchase.date
        }
        result.append(temp)
    return result



def sales_each_product_this_year() -> list:
    """
    Create a list of products and total number of purchases in this year
    """
    # List of dictionaries
    purchases = make_list_of_purchases()
    # Find all sales in this year
    this_year_products = list()
    for purchase in purchases:
        if purchase['Date'].year == (CURRENT_YEAR):
            this_year_products.append(purchase['Product'])

    # Get all products
    all_products = Product.select()

    total_sales = list()

    for product in all_products:
        temp = {
            'Product': product,
            'Purchases': this_year_products.count(product)
        }
        total_sales.append(temp)
    return total_sales


def top_five_sales() -> list:
    """
    Return a list of dictionaries of top most sales in this year
    """
    temp = sales_each_product_this_year()
    top_five = list()

    for i in range(5):
        maximum = max_purchased(purchases=temp)
        top_five.append(maximum)
        temp.remove(maximum)

    return top_five


def get_info_of_top_five():
    """Returns two lists of top five product names and sales"""
    top_five_purchases = top_five_sales()
    names = list()
    purchases = list()
    for purchase in top_five_purchases:
        names.append(purchase['Product'].product_name)
        purchases.append(purchase['Purchases'])
    return names, purchases


def max_purchased(purchases: list) -> dict:
    """Returns a dictionary with must purchase"""
    temp = {
            'Product': None,
            'Purchases': 0
    }
    for purchase in purchases:
        if purchase['Purchases'] > temp['Purchases']:
            temp = purchase
    if temp['Product']:
        return temp
    return purchases[0]


def show_three_diagrams() -> None:
    """
    Shows three diagrams of:
    five most purchased, total number of sales and total money earned
    """
    figure, axis = plt.subplots(1, 3)

    monthly_sale = sale_of_year()
    monthly_earning = earning_of_year()
    names, purchases = get_info_of_top_five()

    months = list(range(1, 13))

    # For monthly sales
    axis[0].bar(months, monthly_sale, color='#081375')
    axis[0].set_title('Monthly Sales')

    # For monthly earning
    axis[1].bar(months, monthly_earning, color='#227508')
    axis[1].set_title('Monthly Earning')

    # For top five sales
    axis[2].bar(names, purchases, color='#47071e')
    axis[2].set_title('Top five sales')

    plt.show()


def create_diagram(y: list, x: list, ylabel: str, titel: str, xlabel: str='Month') -> None:
    """
    Create a diagram of purchases and times
    """
    plt.figure(figsize=(12, 6), num='Chart')
    plt.bar(x, y, color='#47071e', width=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titel)


def pass_arguments():
    """Parses arguments and performs actions based on them."""
    parser = ArgumentParser(add_help=False)
    run_args_help = (
        'Show three diagrams of five most purchased, total number of sales and total money earned.'
    )
    help_args_help = (
        'If you want to see three diagrams you can use -r argument.'
    )
    parser.add_argument('-r', '--report', action='store_true', help=run_args_help)
    parser.add_argument('-h', '--help', action='store_true', help=help_args_help)

    args = parser.parse_args()

    if args.report:
        show_three_diagrams()
    elif args.help:
        parser.print_help()


if __name__ == '__main__':

    if len(sys.argv) > 1:
        pass_arguments()
        sys.exit()

    try:
        # Create tables
        database_manager.create_tables(
            [Customer, Product, ShoppingMall]
        )
        # If there is zero products in database make some
        if len(Product.objects) == 0:
            create_random_product()
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
                case 3:
                    # A customer buys a product
                    while True:
                        customer_id = int(input('Please enter a customer id: '))
                        if customer_exist(customer_id=customer_id):
                            break
                        print('Cannot find this customer! Please try again.')
                    while True:
                        product_id = int(input('Please enter a product id: '))
                        if product_exist(product_id=product_id):
                            break
                        print('Cannot find this product! Please try again.')
                    customer_buy_product(customer=customer_id, product=product_id)
                case 4:
                    # Find a customer by id
                    user_id = int(input('Please enter a customer id: '))
                    if customer_exist(customer_id=user_id):
                        customers = find_customer_by_id(customer_id=user_id)
                        for customer in customers:
                            print(customer)
                            print('-'*20)
                    else:
                        print('Cannot find this customer! Please try again.')
                case 5:
                    # Find product by name
                    name = input('Please enter a product name: ')
                    products = find_product_by_name(product_name=name)
                    for product in products:
                        print(product)
                        print('-'*20)
                case 6:
                    # Find product by id
                    user_id = int(input('Please enter a product id: '))
                    if product_exist(product_id=user_id):
                        products = find_product_by_id(product_id=user_id)
                        for product in products:
                            print(product)
                            print('-'*20)
                    else:
                        print('Cannot find this product! Please try again.')
                case 7:
                    # Show all customers
                    show_all_customers()
                case 8:
                    # Show all products
                    show_all_products()
                case 9:
                    # Create random customers
                    number_of_cus = int(input(
                        'Please enter number of customers you want to randomly create: '
                    ))
                    create_random_customer(count=number_of_cus)
                case 10:
                    # Show top five sales
                    names, purchases = get_info_of_top_five()
                    create_diagram(
                        y=purchases,
                        x=names,
                        ylabel='Number Of Purchases',
                        xlabel='Product Name',
                        titel='Top Five Sales'
                    )
                    plt.show()
                case 11:
                    # Each month sales
                    sales = sale_of_year()
                    create_diagram(
                        y=sales,
                        x=list(range(1, 13)),
                        ylabel='Number Of Sales',
                        titel='Total Sales In A Year'
                    )
                    plt.show()
                case 12:
                    # Total earning each month of a year
                    earnings = earning_of_year()
                    create_diagram(
                        y=earnings,
                        x=list(range(1, 13)),
                        ylabel='Total Earning',
                        titel='Total Earnings In A Year'
                    )
                    plt.show()
                case 13:
                    # Show three diagrams of:
                    # Total earnings of year, total sales of year and top five
                    show_three_diagrams()

    except ValueError as error:
        print(error)
    finally:
        # Closing database connection.
        if database_manager.db:
            database_manager.db.close()
            print('Database connection is closed')
