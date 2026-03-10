# 🚦 Multi-Junction AI Traffic Signal System

An AI-powered traffic management system that uses **YOLOv8 vehicle detection** to dynamically adjust traffic signal timings across multiple junctions.

The system analyzes traffic density from uploaded junction images and intelligently allocates green signal duration to reduce congestion.

---

# 📌 Project Overview

Urban traffic congestion is a major problem in many cities. Traditional traffic signals operate using **fixed timers**, which do not adapt to real-time traffic conditions.

This project introduces an **AI-based adaptive traffic signal system** that:

• Detects vehicles using **YOLOv8 object detection**
• Counts vehicles in **four directions (North, South, East, West)**
• Dynamically assigns **green signal timing based on traffic density**
• Coordinates signals across **multiple junctions** to prevent downstream congestion

The system helps improve **traffic flow efficiency and reduce waiting time**.

---

# 🧠 System Workflow

1️⃣ User uploads traffic images for multiple junctions

2️⃣ YOLOv8 detects vehicles in the images

3️⃣ Vehicles are categorized into directional lanes:

* North
* South
* East
* West

4️⃣ Vehicle counts are calculated for each direction

5️⃣ The AI logic computes optimal **green and red signal durations**

6️⃣ Signal timings are coordinated between junctions to prevent congestion

---

# 🚗 Vehicle Detection

Vehicle detection is performed using the **YOLOv8 object detection model**.

The system detects the following vehicle types from the COCO dataset:

| Class ID | Vehicle Type |
| -------- | ------------ |
| 2        | Car          |
| 3        | Motorbike    |
| 5        | Bus          |
| 7        | Truck        |

Bounding boxes are used to determine the **location of vehicles**, which helps estimate the direction of traffic flow.

---

# ⏱ Signal Timing Logic

The green signal duration is calculated using a **vehicle clearing model**.

Green signal time is determined by:

Green Time = Number of Vehicles × Clearing Time per Vehicle

Example:

If 10 vehicles are waiting and clearing time is **2 seconds per vehicle**:

Green Time = 10 × 2 = **20 seconds**

Safety constraints are applied:

• Minimum green signal time = **15 seconds**
• Maximum green signal time = **60 seconds**

This ensures safe and realistic traffic signal behavior.

---

# 🔄 Multi-Junction Coordination

The system supports **downstream traffic coordination**.

Example logic:

If **Junction 2 West lane is congested**, the system reduces the green time of **Junction 1 East lane** to prevent traffic overflow.

This mimics how **smart city traffic systems coordinate signals** across intersections.

---

# 🖥 System Interface

The system is built using **Streamlit**, which provides an interactive web interface.

Users can:

• Upload images of traffic junctions
• View detected vehicle counts
• See calculated signal timings for each junction

Output includes:

• Vehicle counts by direction
• Signal timings for each phase

---

# 📂 Project Structure

AI-Traffic-Signal-System

main.py → Streamlit application
requirements.txt → Python dependencies
README.md → Project documentation
yolov8n.pt → YOLOv8 model file
sample_images/ → Example traffic images

---

# ⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/AI-Traffic-Signal-System.git

Navigate into the project folder

cd AI-Traffic-Signal-System

Install dependencies

pip install -r requirements.txt

---

# ▶️ Run the Application

Run the Streamlit application using:

streamlit run main.py

After running, open the browser link shown in the terminal:

http://localhost:8501

Upload two junction images to analyze traffic and compute signal timings.

---

# 🛠 Technologies Used

Python
Streamlit
YOLOv8 (Ultralytics)
OpenCV
NumPy

---

# 📊 Example Output

The system produces:

Vehicle Count Example

J1
North: 12
South: 9
East: 5
West: 6

J2
North: 8
South: 11
East: 4
West: 13

Signal Timing Example

J1
Phase A (North-South)
Green: 42 sec
Red: 20 sec

Phase B (East-West)
Green: 20 sec
Red: 42 sec

---

# 🚀 Future Improvements

The system can be extended with advanced AI features:

• Live CCTV traffic feed integration
• LSTM-based traffic prediction
• Emergency vehicle priority system
• Reinforcement learning for signal optimization
• City-scale multi-junction simulation

---

# 🎯 Applications

Smart Cities
Traffic Management Systems
Urban Planning
AI-based Transportation Systems

---

