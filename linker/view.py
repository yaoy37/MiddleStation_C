from fastapi import APIRouter, Request

from common.logger import logger
from linker import logic
from linker import schemas

linker_router = APIRouter()


# 测试wifi模块 地址：http://192.168.10.53/gpio/1

@linker_router.post("/heart_beat_connect", summary="心跳连接接口")
async def heart_beat_connect(fac: schemas.Facility):
    # todo 数据库记录
    logger.info("fac:{}".format(fac))
    # logic.update_facility(fac)
    logic.update_facility_peewee(fac)
    return {"success": "ok", "data": {}}


@linker_router.post("/register", summary="心跳连接接口")
async def heart_beat_connect(request: Request):
    # todo 数据库记录
    request_text = await request.json()
    print("request_text:", request_text)
    return {"success": "ok", "data": {"operation": "post_register"}}


@linker_router.get("/register", summary="心跳连接接口")
async def heart_beat_connect(request: Request):
    # todo 数据库记录
    request_text = await request.body()
    request_text = str(request_text.decode("utf-8"))
    logger.info("request_data:{}".format(request_text))
    return {"success": "ok", "data": {"operation": "get_register"}}
