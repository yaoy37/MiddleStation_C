import uvicorn

from initialize_app import create_app

app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8010, reload=True)
