# 🚀 OrbitLink  
### Earth ↔ Space Communication Simulator  

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![NASA API](https://img.shields.io/badge/API-NASA-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

OrbitLink is a space-themed web application built using Flask that simulates communication between Earth and space systems.  
It integrates real NASA data, live satellite tracking, and interactive UI components.

---

## 🌟 Features

- 🔐 User Login System  
- 📊 Data Visualization Graph  
- 🌌 NASA Astronomy Picture of the Day (APOD)  
- 🛰 Live ISS Satellite Tracking (Real-time Map)  
- 🤖 AI-Based Response Simulation  
- 🌠 Animated Space Background  
- 📱 Fully Mobile Responsive UI  

---

## 🛠 Tech Stack

### Backend
- Python  
- Flask  
- Requests  
- python-dotenv  

### Frontend
- HTML5  
- CSS3  
- JavaScript  
- Leaflet.js  

### APIs Used
- NASA APOD API  
- ISS Live Location API  

---

## 📂 Project Structure

OrbitLink/
│
├── app.py
├── templates/
│   └── index.html
    └── login.html
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙ Installation (Run Locally)

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/OrbitLink.git  
cd OrbitLink  

### 2️⃣ Create Virtual Environment

python3 -m venv venv  
source venv/bin/activate  

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

### 4️⃣ Add NASA API Key

Create a `.env` file and add:

NASA_API_KEY=your_api_key_here  

### 5️⃣ Run Application

python app.py  

Open in browser:

http://127.0.0.1:5000  

---

## 🔐 Security

- API keys are stored securely using environment variables.
- `.env` file is excluded using `.gitignore`.
- Virtual environment is not uploaded.

---

## 📈 Future Improvements

- 🛰 Satellite orbit trail visualization  
- 🌍 Multiple satellite tracking  
- 📡 Live telemetry data (speed, altitude)  
- 🔐 Database-backed authentication  
- 🌐 Public deployment  

---
## 📸 Screenshots

### 🖥 Running from CLI
![CLI](screenshots/running_cli.png)

### 🏠 Homepage + ISS Map
![Homepage](screenshots/homepage_iss.png)

### 🔐 Login Page
![Login](screenshots/login.png)

### 🌌 NASA APOD
![NASA](screenshots/nasa_apod.png)

### 📊 Delay Graph
![Graph](screenshots/delay_graph.png)

### 📡 Transmission Received
![Transmission](screenshots/transmission.png)

## 👨‍💻 Author

Nishant Dubey  
Computer Science Enthusiast 🚀  

---

## ⭐ If You Like This Project

Give it a star on GitHub!
