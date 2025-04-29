# BAJAJ_FINSERV_QUALIFIER2

# 🧪 Lab Report Extraction API (FastAPI + PaddleOCR)

A scalable FastAPI service to process lab report images and automatically extract:
- Lab Test Names
- Test Values
- Units
- Biological Reference Ranges
- Out-of-Range Detection

Built using PaddleOCR for deep learning-based text extraction to handle messy, unstructured hospital reports.

---

## 🚀 How it Works

- Upload an image or PDF of a lab report.
- The API processes it using PaddleOCR.
- Extracts text, detects test values, and matches them against reference ranges.
- Returns structured JSON output instantly.

---

## 📦 Project Structure

```
New_folder/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── paddle_ocr_engine.py
│   ├── parser.py
│   ├── utils.py
├── requirements.txt
├── start.sh
```

---

## ⚙️ Technologies Used

- **FastAPI** — High-performance API backend
- **PaddleOCR** — Deep learning based OCR engine
- **Uvicorn** — ASGI server for FastAPI
- **pdf2image** — PDF to image conversion (for PDF lab reports)
- **OpenCV** — Image preprocessing
- **Python 3.10+**

---

## 📖 Installation

1. Clone this repository or download ZIP.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the server:

```bash
bash start.sh
```

Or manually:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4. Open the API documentation at:

```
http://127.0.0.1:8000/docs
```

---

## 🔥 API Usage

### `POST /get-lab-tests`

**Body:**  
Upload an image or PDF (`multipart/form-data`).

**Response:**  
Returns structured JSON containing lab test details.

---

## 🌎 Deployment Ready

- Easily deployable to Render.com, Railway.app, AWS EC2, or any cloud provider.
- No special hardware required (runs on CPU).

---

## 🤝 Contributions

Pull requests are welcome!  
If you find bugs, have ideas, or want to improve the parser further, feel free to open an issue or PR.

---

## 📜 License

This project is open-source and free to use under the MIT License.
