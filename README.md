# AI Object Detection Platform

A modular project using Python, OpenCV, Ultralytics YOLO, Streamlit, and MySQL.

## Features
- Image upload and YOLO object detection
- Confidence threshold control
- Configurable class filter (comma-separated)
- Annotated detection output
- Optional MySQL event logging
- SQL schema included

## Setup
Recommended: Python 3.10–3.12. MySQL is optional for detection, but required for persistent logging.

```bash
python -m venv .venv
```
Windows Command Prompt:
```bat
.venv\Scripts\activate.bat
```
Install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Run:
```bash
streamlit run app.py
```
Open the local URL shown in the terminal. First run may download `yolov8n.pt`, so internet access may be needed.

## Configure MySQL
1. Start MySQL Server.
2. Run `object_detection_db.sql` in MySQL Workbench.
3. Copy `.env.example` to `.env`.
4. Set your MySQL password in `.env`.
5. Restart the app.

## GitHub
Create a repository on GitHub, then run in this project folder:
```bash
git init
git add .
git commit -m "Build AI object detection platform"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-object-detection-platform.git
git push -u origin main
```
Use the real URL from your GitHub repository. Never upload `.env` or passwords.

## Demo video checklist
1. Show the running app.
2. Upload an image and run detection.
3. Change the object filter and demonstrate it.
4. If MySQL is configured, show the `detection_events` table.
5. Briefly explain `app.py`, `detector.py`, and `database.py`.

## Medium article draft
**Title: Building a Modular AI Object Detection Platform with YOLO, OpenCV, Streamlit, and MySQL**

I built a modular object detection platform that uses YOLO to identify objects in uploaded images. OpenCV handles image processing and annotated output, while Streamlit provides a simple interface. The project includes a configurable object-class filter and a MySQL module for logging image names, detected classes, confidence scores, and timestamps.

The code is separated into modules: `app.py` manages the interface, `detector.py` performs detection and filtering, and `database.py` handles database connectivity and event logging. This modular structure makes the project easier to maintain and extend.

To run it, install the dependencies, configure MySQL if persistent logging is needed, and start the app using `streamlit run app.py`. Publish this article only after testing the project and editing it to accurately reflect your own results.
