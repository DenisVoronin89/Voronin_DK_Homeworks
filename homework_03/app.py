import json

from fastapi import FastAPI, Response, status


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