import sqlite3
from pprint import pprint
# Customers: List of dicts, containing
#   name: String
#   id: int, unique
#   rfid: String
#   credit: float, current financial status

# Products: List of dicts, containing
#   name: String
#   id: int, unique
#   price: float, >0
#   ean13: String, barcode
# Returns list of all products

def run_query(query_text, arg=None):
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    if arg:
        print(query_text)
        print(arg)
        res = cursor.execute(query_text,arg).fetchall()
    else:
        res = cursor.execute(query_text).fetchall()
    cursor.close()
    connection.close()
    return res

def update_db(update_text, arg1, arg2):
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    res = cursor.execute(update_text, (arg1, arg2)).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return


def get_products():
    result = run_query('SELECT * FROM product')
    products = []
    for row in result:
        product = {'id': row[0], 'name':row[1], 'price': float(row[2]), 'ean13': row[3]}
        products.append(product)
    return products


def get_customers():
    result = run_query('SELECT * FROM customer')
    customers = []
    for row in result:
        customer = {'id': row[0], 'name':row[1], 'credit': float(row[2]), 'rfid': row[3]}
        customers.append(customer)
    return customers

# Returns Product by ID, returns None if none found
def get_product_by_id(id):
    result = run_query('SELECT * FROM product WHERE id=?',id)
    result = result[0]
    product = {'id': result[0], 'name': result[1], 'price': float(result[2]), 'ean13': result[3]}
    pprint(product)
    return product

# Returns Product by barcode, returns None if none found
def get_product_by_barcode(barcode):
    return None


# Returns Customer by Barcode, returns None if none found
def get_customer_by_rfid(rfid):
    return None

# Returns Customer by ID, returns None if none found
def get_customer_by_id(id):
    result = run_query('SELECT * FROM customer WHERE id=?',id)
    result = result[0]
    customer = {'id': result[0], 'name': result[1], 'credit': result[2], 'rfid': result[3]}
    return customer

# Processes a sales order.
def buy(customer, product):
    res =get_product_by_id(str(product))
    pprint(res)
    product_price = res["price"]
    update_db('UPDATE customer SET credit = credit - ? WHERE id = ?', float(product_price), str(customer))
    return

def create_user(username, rfid):
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO customer (name, rfid) VALUES ? ?', (username, rfid)).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return None