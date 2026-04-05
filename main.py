from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import cv2
import threading
import time

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the YOLOv8 small model
model = YOLO("yolov8s.pt")

# Global variables for tracking
person_count = 0
frame_to_stream = None
lock = threading.Lock()

def video_capture():
    global person_count, frame_to_stream
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLOv8 inference
        results = model(frame, verbose=False)[0]
        
        current_count = 0
        
        # Draw detections
        for box in results.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label == "person":
                current_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])

                # Draw bounding box (Sleek Green)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 65), 2)
                cv2.putText(frame, f"Person {confidence:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.5, (0, 255, 65), 1)

        with lock:
            person_count = current_count
            # Encode frame to JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_to_stream = buffer.tobytes()

    cap.release()

# Start video capture in a separate thread
capture_thread = threading.Thread(target=video_capture, daemon=True)
capture_thread.start()

@app.get("/video_feed")
def get_video_feed():
    def generate():
        while True:
            with lock:
                if frame_to_stream is not None:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_to_stream + b'\r\n')
            time.sleep(0.01)  # Limit frame rate slightly to reduce CPU usage
            
    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/stats")
def get_stats():
    with lock:
        return {"person_count": person_count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
