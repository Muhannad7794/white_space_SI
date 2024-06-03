from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to the server!"}


@app.get("/firstRouter")
def firstRouter():
    return {"message": "this is the first router!"}
