import cv2

def detect_objects(model, image, confidence_threshold=0.4, class_filter=None):
    class_filter = [x.lower() for x in (class_filter or [])]
    result = model.predict(source=image, conf=confidence_threshold, verbose=False)[0]
    annotated = image.copy()
    detections = []
    if result.boxes is None:
        return annotated, detections
    for box in result.boxes:
        class_id = int(box.cls[0].item())
        name = str(result.names[class_id])
        score = float(box.conf[0].item())
        if class_filter and name.lower() not in class_filter:
            continue
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (40, 220, 80), 2)
        cv2.putText(annotated, f"{name} {score:.2f}", (x1, max(20, y1-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (40, 220, 80), 2)
        detections.append({"class": name, "confidence": round(score, 4)})
    return annotated, detections
