import datetime
import uuid

import peewee

from database_peewee.database_peewee import p_db


class User(peewee.Model):
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField(index=True)
    phone = peewee.CharField(default='')
    description = peewee.CharField(default='')
    status = peewee.IntegerField(index=True, default=0)  # 0正常，1注销
    u_type = peewee.IntegerField(index=True, default=0)  # 0普通用户，1后台用户
    update_time = peewee.DateTimeField(default=datetime.datetime.now)

    @staticmethod
    def update_timestamp(model_class, instance, created):
        instance.updated_at = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.update_timestamp(self.__class__, self, False)
        return super().save(*args, **kwargs)

    class Meta:
        database = p_db
        db_table = 'user'


class UserSession(peewee):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)



p_db.connect()
p_db.create_tables([User])
p_db.close()
