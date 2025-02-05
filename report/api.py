import datetime

from fastapi import APIRouter

from global_var import Var
from schemas import HoleReport

report_router = APIRouter(
    prefix="/report",
    tags=["report"],
)


@report_router.post('/report_hole')
async def report_hole(hole_report: HoleReport):
    await Var.db.add_hole_report(hole_report.lon, hole_report.lat, datetime.datetime.now(), hole_report.locname)
    return {"message": "success"}


@report_router.get('/get_hole_report')
async def get_hole_report():
    return await Var.db.get_hole_report()


@report_router.post('/report_hole')
async def report_hole(hole_report: HoleReport):
    await Var.db.add_hole_report(hole_report.lon, hole_report.lat, datetime.datetime.now(), hole_report.locname)
    return {"message": "success"}


@report_router.post('/report_crash')
async def report_crash(hole_report: HoleReport):
    await Var.db.add_crash_report(hole_report.lon, hole_report.lat, datetime.datetime.now(), hole_report.locname)
    return {"message": "success"}
