import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from peewee import *

DATABASE = SqliteDatabase('charging.db')

class User(UserMixin, Model):
    email = CharField(unique = True)
    phone = CharField(unique = True)
    password = CharField(max_length = 100)

    class Meta:
        database = DATABASE

    def get_charge(self):
        return charge.select().where(charge.user == self)

    @classmethod
    def create_user(cls, email, phone, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    email = email,
                    phone = phone,
                    password = generate_password_hash(password)
                )

        except IntegrityError:
            raise ValueError("Sorry, that user already exists.")

class Charge(Model):
    user = ForeignKeyField(rel_model = User, related_name = "Oakland charging station")
    ID = CharField()
    Device = CharField()
    Terms = BooleanField()
    TD = TextField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.get_conn()
    DATABASE.create_tables([User, Charge], safe=True)
    DATABASE.close()
