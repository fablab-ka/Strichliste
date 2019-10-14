from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable

class customer(BaseTable):
    __table_name__ = 'customers'
    id = IntegerField(primary_key=True, auto_increment=True)
    name = TextField(not_null=True, )
    email = TextField(not_null=True)
    rfid = TextField(not_null=True)
    pin = IntegerField(not_null=True)