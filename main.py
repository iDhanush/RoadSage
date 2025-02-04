from server import app


@app.get("/")
async def root():
    return {"message": "Hello World"}
