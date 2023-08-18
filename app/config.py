import dotenv
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

dotenv.load_dotenv()


@asynccontextmanager
async def lifespan(_: FastAPI):

    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    if not os.path.exists(JSON_FOLDER):
        os.mkdir(JSON_FOLDER)

    if not os.path.exists(IMAGE_FOLDER):
        os.mkdir(IMAGE_FOLDER)

    yield


API_URL = os.getenv("API_URL", "")
API_TITLE = os.getenv("API_TITLE", "")
API_PORT = os.getenv("API_PORT", "")
API_VERSION = os.getenv("API_VERSION", "")
API_HOST = os.getenv("API_HOST", "")
API_SUMMARY = os.getenv("API_SUMMARY", "")
API_DESCRIPTION = os.getenv("API_DESCRIPTION", "")

FASTAPI = dict(
    title=API_TITLE,
    version=API_VERSION,
    summary=API_SUMMARY,
    description=API_DESCRIPTION,
    lifespan=lifespan
)

IMAGE_URL = os.getenv("IMAGE_URL", "")
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER", "")

JSON_FILE = os.getenv("JSON_FILE", "")
JSON_FOLDER = os.getenv("JSON_FOLDER", "")

DATA_FOLDER = os.getenv("DATA_FOLDER", "")

DB_URL = os.getenv("DB_URL", "")
