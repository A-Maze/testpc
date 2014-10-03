from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)

class Component(Document):
    title = StringField(max_length=120, required=True)
    price = StringField(max_length=500, required=True)