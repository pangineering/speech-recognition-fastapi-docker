from typing import Union
from fastapi import FastAPI, File, UploadFile
from numpy import full
from .sr_modules import Google_SR
import logging
import os

app = FastAPI()
log = logging.getLogger(__name__)

DESTINATION = ""
CHUNK_SIZE = 2 ** 20  # 1MB


async def chunked_copy(src, dst):
    await src.seek(0)
    with open(dst, "wb") as buffer:
        while True:
            contents = await src.read(CHUNK_SIZE)
            if not contents:
                log.info(f"Src completely consumed\n")
                break
            log.info(f"Consumed {len(contents)} bytes from Src file\n")
            buffer.write(contents)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/speech-recognition")
async def speech_recognition(file: UploadFile = File(...)):
    fullpath = os.path.join(DESTINATION, file.filename)
    await chunked_copy(file, fullpath)
    sr = Google_SR(audio=fullpath)
    text = sr.use_asr()
    print(fullpath)
    print(text)
    return text