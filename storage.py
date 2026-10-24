import json
import os

FILE = "tickets.json"

def load_tickets():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tickets():
    with open(FILE, "w") as f:
        json.dump(tickets, f, indent=2)