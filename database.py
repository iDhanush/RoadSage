import datetime
import os
import motor.motor_asyncio


class Files_Database:
    def __init__(self):
        _uri = os.environ.get('DB_URI')
        self._client = motor.motor_asyncio.AsyncIOMotorClient(_uri)
        self.db = self._client['roadsage']
        self.holeDB = self.db['holeDB']
        self.crashDB = self.db['crashDB']

    async def add_hole_report(self, lon: float, lat: float, time: datetime.datetime, locname: str):
        await self.holeDB.insert_one({'lon': lon, 'lat': lat, 'time': time, 'locname': locname})

    async def get_hole_report(self):
        await self.holeDB.find({}).sort('time', -1).to_list(None)

    async def add_crash_report(self, lon: float, lat: float, time: datetime.datetime, locname: str):
        await self.crashDB.insert_one({'lon': lon, 'lat': lat, 'time': time, 'locname': locname})

