import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from database import Database
from global_var import Var

app = FastAPI()


@asynccontextmanager
async def lifespan(app2: FastAPI):
    Var.db = Database()
    yield
