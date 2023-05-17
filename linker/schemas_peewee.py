import re
from typing import Any

import peewee
from pydantic import BaseModel
from pydantic import Field, validator
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class Facility(BaseModel):
    index: str = Field(..., description="唯一标识（max地址）")
    sort: str = Field(..., description="类型（z0283,b3884）")
    address: str = Field(..., description="ip地址")
    description: str = Field(..., description="描述信息")
    status: int = Field(..., description=" 状态（0：离线，2：在线 10：初始化）")

    # update: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

    @validator("sort")
    def check_type(cls, sort):
        print("sort:", sort)
        _match = r'^[a_Z]*'
        match = re.match(_match, sort)
        if not match:
            raise ValueError(f'{sort} must start with [a_Z]')
        return sort
