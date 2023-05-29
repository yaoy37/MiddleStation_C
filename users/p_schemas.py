import re
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import Field, validator


class User(BaseModel):
    username: str = Field(..., description="用户账号")
    password: str = Field(..., description="用户密码")
    phone: str = Field(default='', description="ip地址")
    description: str = Field(default='', description="描述信息")
    status: int = Field(default=0, description=" 状态（0正常，1注销）")
    u_type: int = Field(default=0, description=" 状态（0普通用户，1后台用户）")
    update_time: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True

    # @validator("phone")
    # def check_type(cls, phone):
    #     print("sort:", phone)
    #     _match = r'^[a_Z]*'
    #     match = re.match(_match, phone)
    #     if not match:
    #         raise ValueError(f'{phone} must start with [a_Z]')
    #     return phone
