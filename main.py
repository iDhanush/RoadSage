import datetime
from server import app
from global_var import Var
from schemas import HoleReport


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/report_hole')
async def report_hole(hole_report: HoleReport):
    await Var.db.add_hole_report(hole_report.lon, hole_report.lat, datetime.datetime.now(), hole_report.locname)
    return {"message": "success"}


@app.post('/report_crash')
async def report_crash(hole_report: HoleReport):
    await Var.db.add_crash_report(hole_report.lon, hole_report.lat, datetime.datetime.now(), hole_report.locname)
    return {"message": "success"}
