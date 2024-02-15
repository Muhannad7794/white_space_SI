from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/fastapiData")
def root():
    return {"message": [1, 2, 3, 4, 5, 6]}


# define a request function from another server
@app.get("/request2Server")
def request2Server():
    response = requests.get("http://localhost:8080/firstRouter").json()
    return response
