from fastapi import APIRouter, Form
from users import p_schemas as schemas

from common.logger import logger

user_router = APIRouter()


@user_router.post("/register", summary="用户注册")
async def register(username: str = Form(...), password: str = Form(...)):
    # 表单数据 Form
    logger.info("fac:{}".format({"username": username, "password": password}))
    return {"success": "ok", "data": {"get": "success"}}
