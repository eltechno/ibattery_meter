import os
import sys
import time
import psutil
from terminaltables import SingleTable

def get_battery_info():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    health = battery.percent / 100.0
    return plugged, percent, health

def create_bar(value, max_value, width=20):
    bar_length = int((value / max_value) * width)
    return "#" * bar_length + " " * (width - bar_length)

def display_battery_info(plugged, percent, health):
    os.system("clear" if os.name == "posix" else "cls")

    charge_status = "Charging" if plugged else "Not charging"
    health_status = "Healthy" if health > 0.8 else "Not healthy" if health > 0.6 else "Poor"

    battery_table_data = [
        ["Battery State", charge_status],
        ["Battery Level", f"{percent}% {create_bar(percent, 100)}"],
        ["Battery Health", f"{health_status} {create_bar(health * 100, 100)}"]
    ]

    table = SingleTable(battery_table_data)
    table.inner_heading_row_border = False

    print(table.table)

def main():
    while True:
        plugged, percent, health = get_battery_info()
        display_battery_info(plugged, percent, health)
        time.sleep(5)

if __name__ == "__main__":
    main()

