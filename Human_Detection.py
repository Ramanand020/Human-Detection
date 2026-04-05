from ultralytics import YOLO
import cv2

# Load the YOLOv8 small model
model = YOLO("yolov8s.pt")

# Open webcam
cap = cv2.VideoCapture(0)

print("Starting webcam... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)[0]

    # Loop through detections
    for box in results.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        # Only keep 'person' class
        if label == "person":
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("YOLOv8s Human Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
