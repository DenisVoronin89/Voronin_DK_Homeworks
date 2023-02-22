import json

from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse

from views.items import router as items_router
from views.users import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def root():
    data = "<h2>*** WELCOME TO HOMEWORK 03 ***</h2>"
    return HTMLResponse(content=data)


@app.get('/ping')
def ping_message():
    return Response(
        status_code = status.HTTP_200_OK,
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
    )


@app.get('/hello')
def hello(name: str):
    if name is None:
        name = "User"
    data = f"Hello {name}!"
    return Response(content=data, media_type="text/plain")