from fastapi import FastAPI

app = FastAPI()


@app.get("/users/0")
async def read_users():
    return ["Bean", "Elfo"]


@app.get("/users/1")
async def read_users2():
    return ["Rick", "Morty"]