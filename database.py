import os
import motor.motor_asyncio


class Files_Database:
    def __init__(self):
        _uri = os.environ.get('DB_URI')
        self._client = motor.motor_asyncio.AsyncIOMotorClient(_uri)
        self.db = self._client['roadsage']
        self.holeDB = self.db['holeDB']
    async def add_hole_report(self):
