# Customers: List of dicts, containing
#   name: String
#   id: int, unique
#   pin: int[4]
#   rfid: String
#   credit: float, current financial status

# Products: List of dicts, containing
#   name: String
#   id: int, unique
#   price: float, >0
#   ean13: String, barcode

# Returns list of all products
def get_products():
    return []

# Returns Product by ID, returns None if none found
def get_product_by_id(id):
    return None

# Returns Product by barcode, returns None if none found
def get_product_by_barcode(barcode):
    return None

# Returns list of all customers
def get_customers():
    return []

# Returns Customer by Barcode, returns None if none found
def get_customer_by_rfid(rfid):
    return None

# Returns Customer by ID, returns None if none found
def get_customer_by_id(id):
    return None

# Processes a sales order.
def buy(customer, product):
    pass
