"""Summary
"""
import pymysql

conn = None
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

def openConnection():
    global conn
    try:
        if(conn is None):
            pymysql.connect(host='192.168.5.129',
                                 user='root',
                                 password='1234',                             
                                 db='simplehr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        elif (not conn.open):
            pymysql.connect(host='192.168.5.129',
                                 user='root',
                                 password='1234',                             
                                 db='simplehr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)    
    except:
        return Exception

def get_balance(customer):
    """Generates the current balance according to the transactions

    Args:
        customer (int): customer ID

    Returns:
        float: current balance (negative is actually +)
    """
    try:
        openConnection()
        with conn.cursor() as cur:
            res = cur.execute('SELECT sum(amount) FROM transaction WHERE c_id = %s', str(customer)).fetchall()
            cur.close()
            conn.close()
            return res
    except:
        return Exception

def get_products():
    """Summary

    Returns:
        Array[Dict]: returns an array of dicts of the products
    """
    try:
        openConnection()
        with conn.cursor() as cur:
            result = cur.run_query('SELECT * FROM product')
            cur.close()
            conn.close()
    except:
        return Exception
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
    try:
        openConnection
        with conn.cursor() as cur:
            result = cur.run_query('SELECT * FROM customer')
            cur.close()
            conn.close()
    except:
        return Exception
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
    try:
        openConnection()
        with conn.cursor() as cur:
            result = cur.run_query('SELECT * FROM product WHERE id=%s', id)
            cur.close()
            conn.close()
    except:
        return Exception
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
    try:
        openConnection()
        with conn.cursor() as cur:
            result = cur.run_query('SELECT * FROM customer WHERE id=%s', id)
            cur.close()
            conn.close()
    except:
        return Exception
    result = result[0]
    balance = get_balance(id)
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
    try:
        openConnection()
        with conn.cursor() as cur:
            cur.execute('INSERT INTO transaction (c_id, p_id, amount, quantity) VALUES (%s, %s, %s, %s)',(int(customer), int(product), float(price), 1)).fetchall()
            cur.close()
            conn.close()
    except:
        Exception
    return None

def register_transaction(customer, amount):
    """Processes a payment, writes the amount and timestamp for history

    Args:
        customer (int): Customer ID
        amount (float): amount of payment

    Returns:
        None: Success / Fail need to be implemented ###TODO
    """
    try:
        openConnection()
        with conn.cursor() as cur:
            cur.execute('INSERT INTO transaction (c_id, p_id, amount, quantity) VALUES (%s, %s, %s, %s)',(customer, 1, float(amount), 1)).fetchall
            cur.close()
    except:
        Exception
    return None

def create_user(username, rfid):
    """Creates an user

    Args:
        username (String): username
        rfid (String): RFID Card

    Returns:
        None: Success / Fail need to be implemented ###TODO
    """
    try:
        openConnection()
        with conn.cursor() as cur:
            try:
                cur.execute('INSERT INTO customer (name, rfid) VALUES (%s, %s)', (str(username), str(rfid))).fetchall()
            except:
                return False
                #TODO Impleḿent nicer exception
            cur.close()
    except:
        Exception
    return True