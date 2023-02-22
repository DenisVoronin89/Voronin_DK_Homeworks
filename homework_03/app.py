import json

from fastapi import FastAPI, Response, status


@app.get("/")
def root():
    data = "<h2>*** WELCOME TO HOMEWORK 03 ***</h2>"
    return HTMLResponse(content=data)

