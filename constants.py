import jdatetime


CURRENT_YEAR = jdatetime.datetime.now().year


FIRST_NAMES = [
    'Macan', 'Hadi', 'Amir', 'Hassan', 'Hossein', 'Mehran', 'Mehrdad', 'Soroush',
    'Hassan', 'Mina', 'Mehrane', 'Samira', 'Negin', 'Hadis', 'Arman', 'Ahmad', 'Reza',
    'Hamid', 'Mohammad', 'Mohammadreza', 'Ali', 'Mahmod', 'Negar', 'Sarina', 'Armita'
]

LAST_NAMES = [
    'Mehri', 'Khani', 'Amiri', 'Hassani', 'Hosseini', 'Mehrani', 'Mehrdadi', 'Soroushi',
    'Hassani', 'Minai', 'Mehranei', 'Samirai', 'Negini', 'Hadisi', 'Armani', 'Ahmadi', 'Rezai',
    'Hamidi', 'Mohammadi', 'Mohammadrezai', 'Asadi', 'Mahmodi', 'Negari', 'Sarinai', 'Armitai'
]

PRODUCTS = [
    'Pen', 'Book', 'Keyboard', 'Mouse', 'Laptop', 'Mobile', 'Pencil', 'Pencilcase', 'Highlighter',
    'Candle', 'Laser', 'Marker', 'Manitor', 'Handsfree', 'Headset', 'Trashcan', 'Notepad', 'Camera',
    'Paper', 'Doll', 'Glasses', 'Cup', 'Plate', 'Watch'
]

MENU = '''
0. Exit.
1. Add new customer.
2. Add new product.
3. Customer buy a product.
4. Find a customer by id.
5. Find product by name.
6. Find product by id.
7. Show all customers.
8. Show all products.
9. Create random customers.
10. Show a chart of top five sales of a year.
11. Show a chart of total number of sales of a year.
12. Show a chart of total earnings of a year.
13. Show three charts of numbers 10,11,12 in same page.
'''
