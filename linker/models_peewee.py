import datetime

import peewee

from database_peewee.database_peewee import p_db


class Facility(peewee.Model):
    index = peewee.CharField(unique=True, index=True)
    sort = peewee.CharField(index=True)
    address = peewee.CharField()
    description = peewee.CharField()
    status = peewee.IntegerField(index=True, default=1)
    update_time = peewee.DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def update_timestamp(model_class, instance, created):
        instance.updated_at = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.update_timestamp(self.__class__, self, False)
        return super().save(*args, **kwargs)

    class Meta:
        database = p_db
        db_table = 'facility'


p_db.connect()
p_db.create_tables([Facility])
p_db.close()
