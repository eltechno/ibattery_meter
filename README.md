# Mac Battery Monitor

A simple Python script that monitors your Mac battery state, level, health, and charging levels, and displays the information in a bar form in the terminal.

## Prerequisites

- Python 3.x
- `psutil` library (`pip install psutil`)
- `terminaltables` library (`pip install terminaltables`)

You can also install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt

```

#Usage

To run the script, navigate to the directory containing the script and run:

```bash
python battery_monitor.py
```

The script will clear the terminal and update the displayed information every 5 seconds. To stop the script, press Ctrl+C.
