import logging
import os

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from common.exceptions import UnicornException, unicorn_exception_handler, ApiException
from linker.view import linker_router

CURRENT_PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def setup_routers(app: FastAPI):
    app.include_router(linker_router, prefix="/linker", tags=["外部设备"])

    logging.info("*********** 模块URI注册完成 ****************")


def setup_error_handler(app: FastAPI):
    app.add_exception_handler(UnicornException, unicorn_exception_handler)
    app.add_exception_handler(ApiException, lambda request, err: err.to_result())

    async def validation_handler(request: Request, exc: ValidationError):
        return ORJSONResponse(status_code=400, content={'msg': '参数错误', 'errors': exc.errors()})

    app.add_exception_handler(ValidationError, validation_handler)

    async def http_exception_handler(request: Request, exc: HTTPException):
        return ORJSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    app.add_exception_handler(HTTPException, http_exception_handler)

    def handle_exc(request: Request, exc):
        raise exc

    app.add_exception_handler(Exception, handle_exc)


def setup_cors(app: FastAPI) -> None:
    """
    支持跨域
    :param app:
    :return:
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI()

    # 统一异常处理
    setup_error_handler(app)
    # 设置跨域
    setup_cors(app)
    # setup_middleware(app)
    setup_routers(app)

    # setup_nacos(app)

    # 处理数据库连接
    # setup_databases(app)

    @app.on_event('shutdown')
    async def shutdown_connect():
        """
        关闭
        :return:
        """
        logging.info("Server is Shutting down")

    return app
