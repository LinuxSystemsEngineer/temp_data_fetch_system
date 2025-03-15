
# 🌎 Temperature Data Fetch System

**A simple and efficient system to fetch temperature data from the Meteostat API.**  
This lightweight, efficient CLI-based tool allows end-users to retrieve temperature records (high, mid, and low) for a given location over a specific timeline.

---

## ♻️  Supported on multiple operating systems

This program is cross-compatible with multiple operating systems, including Linux, macOS, and Windows.

---

## 📊 Functions

✅ Fetches historical **temperature data** from Meteostat
  
✅ Supports **custom latitude & longitude** input
  
✅ Displays **peak high, mid, and low temperatures**
  
✅ Uses **color-coded terminal output** for readability
  
✅ Automatically aligns data in a **clean, professional format**  

---

## 🛠️ Installation

1. Ensure you have **Python 3.12 or newer** installed on your system.

---

2.  **Clone this GitHub repository**
```bash
git clone https://github.com/LinuxSystemsEngineer/temp_data_fetch_system.git
```

---

3. **Change directories to your newly cloned GitHub repository**
```bash
cd temp_data_fetch_system
```

---

4. **Create a segmented Python virtual environment**
```bash
python3 -m venv .segment
```

---

5. **Activate your segmented Python virtual environment**
---
Linux/macOS
```bash
source .segment/bin/activate
```

---
Windows
```bash
.segment\Scripts\activate
```

---

6.  **Install the required packages**
```bash
pip3 install -r requirements.txt
```

---

7. **Run the program**

```bash
python3 main.py
```
Enter latitude and longitude or press Enter to use default values.

---

🖥️ **Example Output:**
```bash
──────────────────────────────────────────────
Temperature Data Retrieval System
──────────────────────────────────────────────

Enter Latitude (OR press Enter for 38.75 - St. Louis, MO): 
Enter Longitude (OR press Enter for -90.0333 - St. Louis, MO): 

Fetching the nearest weather station...
Fetching historical temperature data from 2013-01-01 to 2023-12-31...

──────────────────────────────────────────────
Temperature Data for:
Lambert-St Louis International Airport (38.75, -90.0333)

Date Range: 2013-01-01 to 2023-12-31
──────────────────────────────────────────────
Peak High Temp:       107.96°F   🔥
Historical Mid Temp:  58.45°F    🌎
Peak Low Temp:        -7.78°F    ❄️
──────────────────────────────────────────────
```

---

📂 **Project Structure**
```bash
/temp_data_fetch_system
│── main.py               # Main program
│── requirements.txt      # Requirements
│── README.md             # Documentation
```
---

🌍 Data Source
This system retrieves data using the [Meteostat API](https://meteostat.net/en/).

---

📜 License

This project is **free and open source** licensed under the **MIT License**.

---
 
