from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('LogFile.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class User(pw.Model):
    wrote_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase, User):
    number = pw.TextField()
    message = pw.TextField()
    name = pw.TextField()
    telegram_id = pw.TextField()