from bottle import Bottle, route, run, template, static_file, request, error, hook, get, post
import bottle
from beaker.middleware import SessionMiddleware
import json
import datetime
import database_sqlite as database

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(bottle.app(), session_opts)

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

def show_error(error_title, error_text="", timeout=5):
    return template('tpl/error.tpl', error_title=error_title, error_text=error_text, timeout=timeout)

@error(500)
def handle_error500(error):
    return show_error("Es ist ein interner Fehler aufgetreten", error)

@get('/')
def main_menu():
    request.session['product'] = None
    request.session['customer'] = None
    return template('tpl/main.tpl', customers=database.get_customers())

@route('/static/<type>/<filename>')
def serve_css(type, filename):
    return static_file(filename, root=type+'/')

@get('/customer/<id>')
def sel_customer(id):
    customer = database.get_customer_by_id(id)
    request.session['customer'] = customer
    return template('tpl/products.tpl', products=database.get_products(), customer=customer)

@route('/confirm')
def confirm():
    database.buy(request.session['customer']['id'], request.session['product']['id'])
    return show_error("Kauf erfolgreich!", timeout=2)

@get('/products')
def products():
    return template('tpl/products.tpl', customer=request.session['customer'], products=database.get_products())

@get('/product/<id>')
def show_product(id):
    product = database.get_product_by_id(id)
    request.session['product'] = product
    return template('tpl/confirm.tpl', product=product, customer=request.session['customer'])

@post('/product_barcode')
def submit_barcode():
    barcode = request.forms.get('barcode')
    product = database.get_product_by_barcode(barcode)
    if product == None:
        return show_error("Barcode nicht gefunden", "Zu diesem Barcode wurde kein Produkt gefunden: " + barcode)
    request.session['product'] = product
    return template('tpl/confirm.tpl',  product=product, customer=request.session['customer'])

@post('/customer_barcode')
def submit_barcode():
    barcode = request.forms.get('barcode')
    customer = database.get_customer_by_rfid(barcode)
    if customer == None:
        return show_error("RFID/Barcode nicht gefunden", "Zu dieser RFID oder Barcode"
                                                         " wurde kein Mitglied gefunden: " + barcode)
    request.session['customer'] = customer
    return template('tpl/product.tpl', product=customer)

@get('/create_customer')
def create_user():
    return template('tpl/create_user.tpl')

@post('/new_user')
def new_user():
    name = request.forms.get('name')
    pin = request.forms.get('pin')
    rfid = request.forms.get('rfid')

#debug(True)
run(app, host='127.0.0.1', port=8081)