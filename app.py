from bottle import Bottle, route, run, debug, template, static_file, request, error
import json
import datetime
import database

app = Bottle()
selected_customer = None
selected_product = None

def show_error(error_title, error_text=""):
    return template('error.tpl', error_title=error_title, error_text=error_text)

def select_product(product):
    global selected_product
    selected_product = product

def select_customer(customer):
    global selected_customer
    selected_customer = customer

@app.error(500)
def handle_error500(error):
    return show_error("Es ist ein interner Fehler aufgetreten", error)

@app.get('/')
def main_menu():
    global selected_product
    selected_product = None
    global selected_customer
    select_customer = None
    return template('main.tpl', customers=database.get_customers())

@app.route('/static/<type>/<filename>')
def serve_css(type, filename):
    return static_file(filename, root=type+'/')

@app.get('/customer/<id>')
def sel_customer(id):
    select_customer(database.get_customer_by_id(id))
    return template('products.tpl', products=database.get_products(), customer=selected_customer)

@app.route('/confirm')
def confirm():
    database.buy(selected_customer['id'], selected_product['id'])
    return show_error("Kauf erfolgreich!")

@app.get('/products')
def products():
    return template('products.tpl', customer=selected_customer, products=database.get_products())

@app.get('/product/<id>')
def show_product(id):
    product = database.get_product_by_id(id)
    select_product(product)
    return template('confirm.tpl', product=selected_product, customer=selected_customer)

@app.post('/product_barcode')
def submit_barcode():
    barcode = request.forms.get('barcode')
    product = database.get_product_by_barcode(barcode)
    if product == None:
        return show_error("Barcode nicht gefunden", "Zu diesem Barcode wurde kein Produkt gefunden.")
    select_product(product)
    return template('confirm.tpl',  product=selected_product, customer=selected_customer)

@app.post('/customer_barcode')
def submit_barcode():
    barcode = request.forms.get('barcode')
    customer = database.get_customer_by_rfid(barcode)
    if customer == None:
        return show_error("RFID/Barcode nicht gefunden", "Zu dieser RFID oder Barcode"
                                                         " wurde kein Mitglied gefunden.")
    select_customer(customer)
    return template('product.tpl', product=customer)


#debug(True)
run(app, host='127.0.0.1', port=8081)