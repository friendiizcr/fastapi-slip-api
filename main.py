import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.post("/decode-qr")
async def decode_qr(file: UploadFile = File(...)):
    # อ่านไฟล์ภาพ
    image_bytes = await file.read()
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # ✅ Decode QR ด้วย OpenCV
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    qr_result = data if data else "No QR code found"

    # ✅ OCR ด้วย pytesseract
    pil_image = Image.open(io.BytesIO(image_bytes))
    ocr_text = pytesseract.image_to_string(pil_image, lang='eng+tha')

    return {
        "qr_result": qr_result,
        "ocr_text": ocr_text
    }

@app.get("/debug")
def debug():
    return {"routes": [route.path for route in app.routes]}
