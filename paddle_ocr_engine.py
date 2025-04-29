from paddleocr import PaddleOCR
import cv2
from .utils import preprocess_image

ocr_model = PaddleOCR(use_angle_cls=False, lang='en', det_db_box_thresh=0.3)
def extract_text_paddleocr(image_path):
    img = preprocess_image(image_path)
    cv2.imwrite("DEBUG_FINAL_IMAGE.png", img)
    print("Image saved as DEBUG_FINAL_IMAGE.png")
    result = ocr_model.ocr("DEBUG_FINAL_IMAGE.png", cls=True)
    lines = []
    if result:
        for idx in range(len(result)):
            res = result[idx]
            if res:
                for line in res:
                    if line:
                        _, (text, confidence) = line
                        if confidence > 0.5:
                            lines.append(text)

    return lines
