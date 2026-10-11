import os
from datetime import datetime
import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO
from detector import detect_objects
from database import init_db, log_detection

st.set_page_config(page_title="AI Object Detection Platform", page_icon="🔎", layout="wide")
st.title("AI Object Detection Platform")
st.write("Upload an image to detect objects with YOLO. MySQL logging is optional.")

with st.sidebar:
    st.header("Detection settings")
    model_path = st.text_input("YOLO model", os.getenv("YOLO_MODEL", "yolov8n.pt"))
    confidence = st.slider("Confidence threshold", 0.10, 0.95, 0.40, 0.05)
    filter_text = st.text_input("Object filter (comma-separated)", "person, car, dog")
    st.caption("Leave blank to include all classes.")
    if st.button("Initialize MySQL table"):
        try:
            init_db()
            st.success("MySQL table is ready.")
        except Exception as exc:
            st.error(f"MySQL setup failed: {exc}")

uploaded = st.file_uploader("Upload image", type=["jpg", "jpeg", "png", "webp"])
if uploaded and st.button("Run Object Detection", type="primary"):
    image = cv2.imdecode(np.frombuffer(uploaded.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        st.error("Could not read the image.")
    else:
        try:
            with st.spinner("Detecting objects..."):
                model = YOLO(model_path)
                filters = [x.strip().lower() for x in filter_text.split(",") if x.strip()]
                annotated, detections = detect_objects(model, image, confidence, filters)
            st.image(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB), caption="Detection result", use_container_width=True)
            if detections:
                st.subheader("Detected objects")
                st.dataframe(detections, use_container_width=True)
                try:
                    init_db()
                    for item in detections:
                        log_detection(uploaded.name, item["class"], item["confidence"], datetime.now())
                    st.success(f"Logged {len(detections)} event(s) to MySQL.")
                except Exception as exc:
                    st.warning(f"Detection succeeded, but MySQL logging is unavailable: {exc}")
            else:
                st.info("No objects matched the selected filter.")
        except Exception as exc:
            st.error(f"Detection failed: {exc}")
            st.info("The first run may need internet access to download the YOLO model.")
st.caption("MySQL logging requires a running MySQL server and credentials in your .env file.")
