from storage import load_tickets 
from storage import save_tickets 
from validation import get_input 

def create_ticket():
    tickets = load_tickets()
    ticket = {
        "id": max((t["id"] for t in tickets), default=0) + 1,
        "title": get_input("Title: ")
        "description": get_input("Description: ")
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print(f"Ticket #{ticket['id']} created.")