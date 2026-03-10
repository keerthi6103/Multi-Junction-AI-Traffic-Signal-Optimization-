import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import copy

 CONFIG 
model = YOLO("yolov8n.pt")

vehicle_classes = [2, 3, 5, 7]  # car, motorbike, bus, truck
min_green = 15
max_green = 60
threshold = 0.5


 VEHICLE DETECTION 
def detect_vehicles(uploaded_file):

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    height, width, _ = frame.shape
    counts = {"North": 0, "South": 0, "East": 0, "West": 0}

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls in vehicle_classes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                if cy < height // 2 and abs(cx - width//2) < width//4:
                    counts["North"] += 1
                elif cy >= height // 2 and abs(cx - width//2) < width//4:
                    counts["South"] += 1
                elif cx >= width // 2:
                    counts["East"] += 1
                else:
                    counts["West"] += 1

    return counts


# ---------------- SIGNAL LOGIC ----------------
def compute_signal(j1, j2):

    state = copy.deepcopy({"J1": j1, "J2": j2})


    # Downstream Coordination (J1 → J2)
 
    j2_west_count = state["J2"]["West"]

    if j2_west_count > 10:   # simple congestion threshold
        state["J1"]["East"] = max(1, int(state["J1"]["East"] * 0.5))

    results = {}

    for name, data in state.items():

       # Realistic Vehicle-Clearing Logic
     
        clearing_time_per_vehicle = 2  # seconds per vehicle

        phase_A_count = data["North"] + data["South"]
        phase_B_count = data["East"] + data["West"]

        green_A = phase_A_count * clearing_time_per_vehicle
        green_B = phase_B_count * clearing_time_per_vehicle

        # Safety constraints
        green_A = max(min_green, min(green_A, max_green))
        green_B = max(min_green, min(green_B, max_green))

        # Red time automatically opposite phase
        red_A = green_B
        red_B = green_A

        results[name] = {
            "Phase A (North-South)": {
                "Green": round(green_A, 1),
                "Red": round(red_A, 1)
            },
            "Phase B (East-West)": {
                "Green": round(green_B, 1),
                "Red": round(red_B, 1)
            }
        }

    return results


# ---------------- STREAMLIT UI ----------------
st.title("🚦 Multi-Junction AI Traffic Signal System")
st.subheader("Upload Junction Images")

j1_image = st.file_uploader("Upload J1 Image", type=["jpg", "png"])
j2_image = st.file_uploader("Upload J2 Image", type=["jpg", "png"])

if j1_image and j2_image:

    st.info("Running YOLO Detection...")

    j1_counts = detect_vehicles(j1_image)
    j2_counts = detect_vehicles(j2_image)

    st.write("### 🚗 J1 Vehicle Count")
    st.json(j1_counts)

    st.write("### 🚗 J2 Vehicle Count")
    st.json(j2_counts)

    signal_results = compute_signal(j1_counts, j2_counts)

    st.write("## 🚦 Coordinated Signal Timings")

    for junction, timings in signal_results.items():
        st.write(f"### {junction}")
        st.json(timings)
