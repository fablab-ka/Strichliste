products = [
    {'id': 0, 'name':'Club Mate', 'price': 1, 'ean13': 'asd'},
    {'id': 1, 'name':'Premium Cola', 'price':1,'ean13':'dsa'},
    {'id': 2, 'name':'Tannenzäpfle', 'price':1.5,'ean13':'sad'},
    {'id': 3, 'name':'Fritz Cola Zitrone', 'price':1,'ean13':'4260107220077'},
    {'id': 4, 'name':'Fritz Cola Orange', 'price':1,'ean13':'4260107220114'},
    {'id': 5, 'name':'Fritz Cola Honigmelone', 'price':1,'ean13':''},
    {'id': 6, 'name':'Apfelsaft', 'price':1,'ean13':''},
    {'id': 7, 'name':'Mineralwasser', 'price':1,'ean13':''},
    {'id': 8, 'name':'Eis', 'price':0.5,'ean13':''},
]

customers = [
<<<<<<< Updated upstream
    {'id': 0, 'name': 'Philip C', 'credit': 0, 'rfid': 'asd'},
=======
    {'id': 0, 'name': 'Philip C', 'credit': 0, 'rfid': 'asdf'},
>>>>>>> Stashed changes
    {'id': 1, 'name': 'Max M', 'credit': 0, 'rfid': ''},
    {'id': 2, 'name': 'Lukas 3', 'credit': 0, 'rfid': ''},
    {'id': 3, 'name': 'Otto O', 'credit': 0, 'rfid': ''},
]

sales = []

def get_products():
    return products

def get_product_by_id(id):
    for product in products:
        if product['id'] == int(id):
            return product
    return None

def get_product_by_barcode(barcode):
    for product in products:
        if product['ean13'] == str(barcode):
            return product
    return None

def get_customers():
    return customers

def get_customer_by_rfid(rfid):
    for customer in customers:
        if customer['rfid'] == str(rfid):
            return customer
    return None

def get_customer_by_id(id):
    for customer in customers:
        if customer['id'] == int(id):
            return customer
    return None

def buy(customer, product):
    sales.append({'customer'})
    get_customer_by_id(customer)['credit'] -= get_product_by_id(product)['price']
