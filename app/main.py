import uvicorn
from typing import Union, Annotated
from fastapi import FastAPI, Header, HTTPException, Request


app = FastAPI()


valid_keys = ['abcdef', 'ghijkl', 'mnopqr']


# Route for docker healthcheck
@app.get("/healthcheck", include_in_schema=False)
async def healthcheck(request: Request):
    #logger.debug("Healthcheck called.")
    return {"status": "healthy"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}


@app.get("/auth/", status_code=200)
async def read_items(auth: Annotated[Union[str, None], Header()] = None):
    if auth not in valid_keys:
        raise HTTPException(status_code=401, detail="Invalid Key")
    return {"Result": ':)'}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")