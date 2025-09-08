from fastapi import FastAPI, File, UploadFile
from PIL import Image
from pyzbar.pyzbar import decode
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.post("/decode-qr")
async def decode_qr(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    qr_data = decode(image)

    if not qr_data:
        return {"result": "No QR code found"}

    return {"result": qr_data[0].data.decode("utf-8")}
