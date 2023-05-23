from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('LogFile.db')


class ModelBase(pw.Model):

    class Meta():
        database = db


class History(ModelBase):
    user_id = pw.IntegerField()
    message = pw.TextField()
    command = pw.TextField()
    created_at = pw.DateField(default=datetime.now())