from fastapi import APIRouter, Form
from users import p_schemas as schemas
from users import logic
from common.logger import logger

user_router = APIRouter()


@user_router.post("/register", summary="用户注册")
async def register(username: str = Form(...), password: str = Form(...)):
    # 表单数据 Form
    logger.info("register:{}".format({"username": username, "password": password}))
    _u = schemas.User(**{"username": username, "password": password})
    await logic.create_user(_u)
    return {"success": "ok", "data": {"register": "success"}}


@user_router.post("/login", summary="登录")
async def login(username: str = Form(...), password: str = Form(...)):
    logger.info("login:{}".format({"username": username, "password": password}))
    return {"success": "ok", "data": {"login": "success"}}
