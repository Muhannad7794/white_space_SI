from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from datetime import datetime
import asyncio

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def serv_root_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

async def dateTime():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yield f"data: {now}\n\n"
        await asyncio.sleep(1)
        
@app.get("/sse")
def dateTimeGenerator():
    return StreamingResponse(dateTime(), media_type="text/event-stream")