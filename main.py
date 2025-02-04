from server import app


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/report_hole')
async def report_hole():
    pass