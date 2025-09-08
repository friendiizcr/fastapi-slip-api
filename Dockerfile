# ✅ ใช้ Python base image
FROM python:3.10

# ✅ ติดตั้ง Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# ✅ ตั้ง working directory
WORKDIR /app

# ✅ คัดลอกไฟล์ทั้งหมดเข้า container
COPY . /app

# ✅ ติดตั้ง Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ รัน FastAPI ด้วย Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
