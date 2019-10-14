from peewee import *

database = SqliteDatabase('datenbank.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Customer(BaseModel):
    email = TextField(null=True, unique=True)
    name = TextField(unique=True)
    pin = IntegerField(null=True)
    rfid = TextField(null=True, unique=True)

    class Meta:
        table_name = 'customer'

class Product(BaseModel):
    ean = TextField(null=True)
    name = TextField()
    price = FloatField()

    class Meta:
        table_name = 'product'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class Transaction(BaseModel):
    amount = FloatField()
    c = ForeignKeyField(column_name='c_id', field='id', model=Customer)
    p = ForeignKeyField(column_name='p_id', field='id', model=Product)
    quantity = IntegerField()
    ts = DateField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'transaction'

