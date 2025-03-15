#!/usr/bin/env python3

import os
import pandas as pd
from meteostat import Stations, Daily
from datetime import datetime
import sys

# Function to clear the screen (Linux & Windows compatible)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear screen before starting
clear_screen()

# ANSI escape codes for colored text
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Modern, clean separator
SEPARATOR = "──────────────────────────────────────────────"

print(f"{Colors.HEADER}{SEPARATOR}")
print(f"{Colors.BOLD}Temperature Data Retrieval System{Colors.RESET}")
print(f"{Colors.HEADER}{SEPARATOR}{Colors.RESET}")

# ✅ Default coordinates for St. Louis, MO
DEFAULT_LAT = 38.75
DEFAULT_LON = -90.0333

# ✅ Get user input for location with default values
try:
    lat_input = input(f"{Colors.BLUE}Enter Latitude (OR press Enter for {DEFAULT_LAT} - St. Louis, MO): {Colors.RESET}").strip()
    lon_input = input(f"{Colors.BLUE}Enter Longitude (OR press Enter for {DEFAULT_LON} - St. Louis, MO): {Colors.RESET}").strip()

    # Use default values if the user presses Enter
    lat = float(lat_input) if lat_input else DEFAULT_LAT
    lon = float(lon_input) if lon_input else DEFAULT_LON

except ValueError:
    print(f"{Colors.RED}Invalid input! Please enter numeric latitude and longitude values.{Colors.RESET}")
    sys.exit(1)

print(f"\n{Colors.YELLOW}Fetching the nearest weather station...{Colors.RESET}")
stations = Stations().nearby(lat, lon)
stations = stations.fetch(5)

if stations.empty:
    print(f"{Colors.RED}No weather stations found near the given coordinates! Please try again.{Colors.RESET}")
    sys.exit(1)

# ✅ Select the closest actual station
station = stations.iloc[0]  
station_name = " ".join(station["name"].split())  # Fix double spaces
station = pd.DataFrame([station])  

# ✅ Set date range for data retrieval (Fixed to avoid warnings)
start = datetime(2013, 1, 1)
end = datetime(2023, 12, 31)

print(f"{Colors.YELLOW}Fetching historical temperature data from {start.date()} to {end.date()}...{Colors.RESET}")
daily_data = Daily(station, start=start, end=end).fetch()

# ✅ Fix for FutureWarning: Ensure explicit datetime conversion
if not daily_data.empty:
    daily_data.reset_index(inplace=True)  # Ensure index is a normal column
    daily_data['time'] = pd.to_datetime(daily_data['time'], errors='coerce')  # Explicitly convert to datetime
    daily_data.set_index('time', inplace=True)  # Set it back as index

    # Drop rows with NaN values
    daily_data = daily_data.dropna(subset=['tmax', 'tmin'])
    
    if not daily_data.empty:
        # ✅ Calculate peak temperatures
        peak_high = daily_data['tmax'].max()  
        peak_low = daily_data['tmin'].min()   
        historical_mid_range = ((daily_data['tmax'] + daily_data['tmin']) / 2).mean()  

        # Convert Celsius to Fahrenheit
        peak_high_fahrenheit = (peak_high * 9/5) + 32
        peak_low_fahrenheit = (peak_low * 9/5) + 32
        historical_mid_range_fahrenheit = (historical_mid_range * 9/5) + 32

        # ✅ Display Results
        print(f"\n{Colors.GREEN}{SEPARATOR}")
        print(f"{Colors.BOLD}Temperature Data for:{Colors.RESET}")
        print(f"{station_name} ({lat}, {lon})")
        print(f"\n{Colors.BOLD}Date Range:{Colors.RESET} {start.date()} to {end.date()}")
        print(f"{Colors.GREEN}{SEPARATOR}{Colors.RESET}")

        # ✅ Fixed-Width Formatting for Perfect Alignment
        print(f"{Colors.BOLD}{'Peak High Temp:'.ljust(25)}{str(round(peak_high_fahrenheit, 2)).rjust(10)}°F  🔥")
        print(f"{Colors.BOLD}{'Historical Mid Temp:'.ljust(25)}{str(round(historical_mid_range_fahrenheit, 2)).rjust(10)}°F  🌎")
        print(f"{Colors.BOLD}{'Peak Low Temp:'.ljust(25)}{str(round(peak_low_fahrenheit, 2)).rjust(10)}°F  ❄️")

        print(f"{Colors.GREEN}{SEPARATOR}{Colors.RESET}\n")

    else:
        print(f"{Colors.RED}No valid temperature data found for the selected station and date range.{Colors.RESET}")
else:
    print(f"{Colors.RED}No data found for the selected station and date range.{Colors.RESET}")

