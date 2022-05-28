# uvicorn main:app --reload

from fastapi import FastAPI
from urllib.parse import urlparse
import matplotlib

# matplotlib.use("TKAgg")
matplotlib.use("agg") # matplotlib.use("macOSX")

from matplotlib import pyplot as plt # import matplotlib.pyplot as plt

import numpy as np
from PIL import Image
from wordcloud import STOPWORDS, WordCloud
import io
import urllib, base64

def word_cloud(text):
    whale_mask = np.array(Image.open("cloud.png"))
    # stopwords ={'은','입니다'}
    stopwords = set(STOPWORDS)
    # plt.figure(figsize = (20,5))
    # font_path = 'C:/Users/Jeong Suji/NanumBarunGothic.ttf'
    wc = WordCloud(background_color = 'white', max_words=1000, mask = whale_mask, stopwords = stopwords,
                   prefer_horizontal=0.5, mode="RGBA")
    wc= wc.generate(text)
    plt.figure(figsize=[20,10])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")

    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_64

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

