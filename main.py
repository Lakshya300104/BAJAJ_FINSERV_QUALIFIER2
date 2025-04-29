from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse
import shutil
import os
from pdf2image import convert_from_path
from app.paddle_ocr_engine import extract_text_paddleocr
from app.parser import parse_lab_results

app = FastAPI()

def convert_pdf_to_image(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)
    first_page = pages[0]
    temp_img_path = "temp_converted_image.png"
    first_page.save(temp_img_path, 'PNG')
    return temp_img_path

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs#/default/get_lab_tests_get_lab_tests_post")

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if file.filename.lower().endswith(".pdf"):
            temp_img_path = convert_pdf_to_image(temp_path)
            ocr_lines = extract_text_paddleocr(temp_img_path)
            os.remove(temp_img_path)
        else:
            ocr_lines = extract_text_paddleocr(temp_path)

        os.remove(temp_path)

        structured_data = parse_lab_results(ocr_lines)

        print("---- OCR LINES ----")
        for line in ocr_lines:
            print(line)
        print("-------- END --------")

        return {
            "is_success": True,
            "data": structured_data
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "is_success": False,
            "data": [],
            "error": str(e)
        })
