# uvicorn main:app --reload

from cgitb import handler
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,StreamingResponse
from typing import Optional
from fastapi import APIRouter, Depends,Query
import matplotlib
from pyparsing import Optional

# matplotlib.use("TKAgg")
# matplotlib.use("agg") 
# matplotlib.use("macOSX")

from matplotlib import pyplot as plt # import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
from wordcloud import STOPWORDS, WordCloud
import io
import urllib, base64
from mangum import Mangum

tags_metadata = [
    {
        "name": "",
        "description": "",
        "externalDocs": {
            "description": "Contact me tc.onyemaobi@gmail.com ",
            "url": "https://camlds.com",
        },
    },
]

app = FastAPI(
    title="Collins Word Cloud",
    description="High Perfomance Endpoints ",
    version="1.0",
    openapi_tags=tags_metadata,
    docs_url="/docs", redoc_url="/re",
    openapi_url="/cwc/api/v1/coreapi.json",
    log_config=None
)

# app.add_middleware(
# CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
# )




@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)