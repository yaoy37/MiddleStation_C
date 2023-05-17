import re
import datetime
from pydantic import BaseModel, Field, validator
from sqlalchemy.orm import Session

from linker.models import Facility as fac


class Facility(BaseModel):
    index: str = Field(..., description="唯一标识（max地址）")
    sort: str = Field(..., description="类型（z0283,b3884）")
    address: str = Field(..., description="ip地址")
    description: str = Field(..., description="描述信息")
    status: int = Field(..., description=" 状态（0：离线，2：在线 10：初始化）")
    update_time = datetime.datetime.now()

    class Config:
        orm_mode = True

    @validator("sort")
    def check_type(cls, sort):
        _match = r'^[a-zA-Z]'
        match = re.match(_match, sort)
        if not match:
            raise ValueError(f'{sort} must start with [a_Z]')
        return sort


def create_user(facility: Facility):
    # db_facility = Facility(index=facility.index, sort=facility.sort, address=facility.address,
    #                        description=facility.description, status=facility.status)
    print("db_facility:", type(facility), facility)
    aa = fac(**facility.dict())
    print("db_facility:", type(aa), aa)
    Session().add(aa)
    # a = Facility(**facility.dict())
    return facility
