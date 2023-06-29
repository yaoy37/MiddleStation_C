import peewee
from users import p_schemas, p_models


async def create_user(fac: p_schemas.User):
    print("create_user:", type(fac), fac)
    _obj = p_models.User.select().where(p_models.User.username == fac.username).first()
    if _obj:
        up_data = fac.dict()
        up_data.pop("username")
        p_models.User.update(up_data).where(p_models.User.username == fac.username).execute()
    else:
        n_m = p_models.User(**fac.dict())
        n_m.save()
