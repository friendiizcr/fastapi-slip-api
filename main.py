import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/decode-qr")
async def decode_qr(file: UploadFile = File(...)):
    image_bytes = await file.read()
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if not data:
        return {"result": "No QR code found"}

    return {"result": data}

@app.get("/debug")
def debug():
    return {"routes": [route.path for route in app.routes]}
