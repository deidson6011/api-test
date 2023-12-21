from fastapi import FastAPI, Request
import socket


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/who")
def who_am_i():
    host_name = socket.gethostname()
    return {"This is": host_name}


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck(request: Request):
    return {"status": "healthy"}


if __name__ == '__main__':
    uvicorn.run("main:app", port=5001, log_level="info")
