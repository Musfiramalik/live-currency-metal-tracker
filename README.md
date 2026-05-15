#  Live Currency & Precious Metal Tracker

##  Project Overview
This is a Python-based real-time price tracking system that displays live currency exchange rates and precious metal prices in Pakistani Rupees (PKR). It uses API data and console visualization to show updated values dynamically.

---

##  Features
- Live currency price tracking (USD, EUR, SAR)
- Precious metal price simulation (Gold & Silver)
- Real-time updates every 5 seconds
- Clean console table display using Rich library
- Currency conversion to PKR
- Continuous live monitoring system

---

## Technologies Used
- Python
- requests (API handling)
- time (refresh system)
- rich (console table UI)
- CoinGecko API (currency data source)

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Musfiramalik/live-currency-metal-tracker.git
```

### 2. Move into project folder
```bash
cd live-currency-metal-tracker
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

##  requirements.txt
Make sure your `requirements.txt` contains:

```txt
requests
rich
```

---

##  How to Run

```bash
python main.py
```

---

##  Output
- Displays a live table of currency and metal prices
- Updates automatically every 5 seconds
- Runs continuously until stopped (Ctrl + C)
- <img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/df473dda-5a8d-4c32-843e-a3cfda1556e5" />


---

## Important Notes
- Internet connection is required for live currency data
- Metal prices are currently simulated (can be replaced with API key)
- API limits may affect real-time updates

---

## Future Improvements
- Add real metal API integration
- Graph visualization of price trends
- Web dashboard version (Flask/Django)
- Historical price tracking

---

## Author
Musfira Malik  
GitHub: https://github.com/Musfiramalik  
```
