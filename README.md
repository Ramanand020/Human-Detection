![Python](https://img.shields.io/badge/Python-3.8-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-red)
# 🧠 Human Detection  using YOLOv8 + FastAPI

A real-time Human Detection System powered by YOLOv8, with a modern web dashboard to visualize live video feed and detection statistics.

---

## 🚀 Features
- 🔍 Real-time human detection using YOLOv8
- 🎥 Live webcam video streaming
- 📊 Dashboard with person count and activity logs
- ⚡ FastAPI backend for high-performance streaming
- 🌐 Interactive frontend (HTML, CSS, JS)
- 📈 Live updates every second

---

## 🛠️ Tech Stack
### Backend
- Python
- FastAPI
- OpenCV
- Ultralytics YOLOv8

### Frontend
- HTML
- CSS
- JavaScript
---

## 📂 Project Structure
```
human-detection-project/
│
├── main.py               # FastAPI backend server
├── Human_Detection.py    # Standalone detection script
├── yolov8s.pt            # YOLOv8 model
├── index.html            # Frontend UI
├── style.css             # Styling
├── script.js             # Frontend logic
├── README.md             # Project documentation
```

---

## ⚙️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ramanand020/Human-Detection.git
cd Human-Detection
```
### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn opencv-python ultralytics
```

## ▶️ How to Run
### Start backend:
```bash
python main.py
```
 Server will start at:
 ```
 http://localhost:8000
 ```
 ### Open Frontend
 Simply open:
 ``` 
 index.html
 ```
 in your Browser
 ## 📡 API Endpoints
 ### 🎥 Video Feed
 ```
 GET /video_feed
 ```
 - Streams real-time video with detection
 ## 📊 Stats
 ```
 GET /stats
 ```
 - Returns:
 ```json
 {
  "person_count": 3
}
```
## 🧠 How It Works
- YOLOv8 model detects objects from webcam frames
- Only "person" class is filtered and counted
- Backend streams processed frames using FastAPI
- Frontend fetches stats every second and updates UI

## 📸 Dashboard Preview
- Live camera feed
- Real-time person count
- Activity logs
- System status indicator
## 🧪 Alternative Script
You can also run detection directly without dashboard:
```bash
python Human_Detection.py
```
This will:
- Open webcam
- Detect humans
- Display bounding boxes
## Requirements
- Python 3.8+
- Webcam
- Internet (for initial model download if not present)
## 💡 Future Improvements
- Add face recognition
- Save detection logs to database
- Deploy on cloud (AWS / Azure)
- Mobile app integration
- Multi-camera support
## 👨‍💻 Author
Ramanand Jha
## 📜 License
This project is for educational purposes.
