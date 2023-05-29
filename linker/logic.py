from linker import schemas, models_peewee, models

from database.dependencies import get_db


def update_facility(fac: schemas.Facility):
    """使用共框架原生的orm结构，每次需要主动获取 db session,
    :param fac:
    :return:
    """
    db = next(get_db())

    _obj = db.query(models.Facility).filter(models.Facility.index == fac.index).first()
    if _obj:
        up_data = fac.dict()
        up_data.pop("index")
        db.query(models.Facility).filter(models.Facility.index == fac.index).update(up_data)
    else:
        n_m = models.Facility(**fac.dict())
        db.add(n_m)
    db.commit()


def update_facility_peewee(fac: schemas.Facility):
    """使用peewee插件实现orm,它会帮助获取数据库对象
    :param fac:
    :return:
    """
    print("update_facility_peewee:", type(fac), fac)
    _obj = models_peewee.Facility.select().where(models_peewee.Facility.index == fac.index).first()
    print(_obj)
    if _obj:
        up_data = fac.dict()
        up_data.pop("index")
        models_peewee.Facility.update(up_data).where(models_peewee.Facility.index == fac.index).execute()
    else:
        n_m = models_peewee.Facility(**fac.dict())
        n_m.save()


if __name__ == '__main__':
    # a = list(models_peewee.FacilityV1.filter(models_peewee.FacilityV1.index == "A0:20:A6:23:83:96"))
    # a = models_peewee.FacilityV1.filter(models_peewee.FacilityV1.index == "swewe").first()
    a = list(models_peewee.Facility.select().where(models_peewee.Facility.index == "A0:20:A6:23:83:96"))
    a = models_peewee.Facility.select()
    print(list(a))
    for i in a:
        print(i.index, i.description)
