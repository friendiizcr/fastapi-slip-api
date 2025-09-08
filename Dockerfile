FROM python:3.10

# ✅ ติดตั้ง Tesseract OCR และ libGL สำหรับ OpenCV
RUN apt-get update && apt-get install -y tesseract-ocr libgl1 tesseract-ocr-tha

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
