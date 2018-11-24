"""Summary
"""
import sqlite3
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
    """runs basic sql querys, including opening and closing the connection

    Args:
        query_text (Strin): Select / other basic statement with a single parameter
        arg (None, optional): optional parameter

    Returns:
        object: Description
    """
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    if arg:
        res = cursor.execute(query_text, arg).fetchall()
    else:
        res = cursor.execute(query_text).fetchall()
    cursor.close()
    connection.close()
    return res

def get_balance(customer):
    """Generates the current balance according to the transactions

    Args:
        customer (int): customer ID

    Returns:
        float: current balance (negative is actually +)
    """
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    res = cursor.execute('SELECT sum(amount) FROM `transaction` WHERE c_id = ?', str(customer)).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return res


def get_products():
    """Summary

    Returns:
        Array[Dict]: returns an array of dicts of the products
    """
    result = run_query('SELECT * FROM product')
    products = []
    for row in result:
        if row[0] == 1:
            continue
        product = {'id': row[0], 'name':row[1], 'price': float(row[2]), 'ean13': row[3]}
        products.append(product)
    return products


def get_customers():
    """returns an array of dicts with the customers

    Returns:
        Array[Dict]: returns an array of dicts of the customers
    """
    result = run_query('SELECT * FROM customer')
    customers = []
    for row in result:
        if row[0] == 1:
            continue
        customer = {'id': row[0], 'name':row[1], 'credit': 0, 'rfid': row[2]}
        customers.append(customer)
    return customers

def get_product_by_id(id):
    """Returns product by ID, returns None if none found

    Args:
        id (int): Prodict ID

    Returns:
        Dict: id, name, price, barcode
    """
    result = run_query('SELECT * FROM product WHERE id=?', id)
    result = result[0]
    product = {'id': result[0], 'name': result[1], 'price': float(result[2]), 'ean13': result[3]}
    return product

def get_product_by_barcode(barcode):
    """Returns product by barcode, returns None if none found

    Args:
        barcode (TYPE): Description

    Returns:
        TYPE: Description ###TODO: needs to be implemented
    """
    return None


# Returns Customer by Barcode, returns None if none found
def get_customer_by_rfid(rfid):
    """Returns customer by barcode, returns None if none found

    Args:
        rfid (String): RFID card

    Returns:
        Dict: id, name, current balance, rfid ###TODO: needs to be implemented
    """
    return None

# Returns Customer by ID, returns None if none found
def get_customer_by_id(id):
    """Returns customer by ID, returns None if none found

    Args:
        id (int): customer ID

    Returns:
        Dict: id, name, current balance, rfid
    """
    result = run_query('SELECT * FROM customer WHERE id=?', id)
    result = result[0]
    balance = get_balance(id)[0][0]
    if not balance:
        balance = 0.0
    customer = {'id': id, 'name': result[1], 'credit': balance, 'rfid': result[2]}    ### FIXM
    return customer

def pay(customer, product):
    """Processes a sales order, writes the current price and timestamp for history

    Args:
        customer (int): Customer ID
        product (int): Prodict ID

    Returns:
        None: Success / Fail need to be implemented ###TODO
    """
    res = get_product_by_id(str(product))
    price = res['price']
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO `transaction` (c_id, p_id, amount, quantity) VALUES (?, ?, ?, ?)',(int(customer), int(product), float(price), 1)).fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return None

def register_transaction(customer, amount):
    """Processes a payment, writes the amount and timestamp for history

    Args:
        customer (int): Customer ID
        amount (float): amount of payment

    Returns:
        None: Success / Fail need to be implemented ###TODO
    """
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO `transaction` (c_id, p_id, amount, quantity) VALUES (?, ?, ?, ?)',
                   (customer, 1, float(amount), 1)).fetchall
    connection.commit()
    cursor.close()
    connection.close()
    return None

def create_user(username, rfid):
    """Creates an user

    Args:
        username (String): username
        rfid (String): RFID Card

    Returns:
        None: Success / Fail need to be implemented ###TODO
    """
    connection = sqlite3.connect('datenbank.db')
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO customer (name, rfid) VALUES (?, ?)', (str(username), str(rfid))).fetchall()
    except:
        return False
        #TODO Impleḿent nicer exception
    connection.commit()
    cursor.close()
    connection.close()
    return True
