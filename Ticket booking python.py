import random
import re

class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    @staticmethod
    def generate_customer_id():
        random_id = random.randint(1000, 9999)
        return f"TICK{random_id}"

    @staticmethod
    def verify_customer_id(customer_id):
        pattern = r"^TICK\d{4}$"
        return re.match(pattern, customer_id) is not None


class TicketBooking:
    def __init__(self):
        self.events = {
            "Concert": {"price": 50, "seats": 100},
            "Theater": {"price": 40, "seats": 75},
            "Sports": {"price": 60, "seats": 50},
        }
        self.booked_tickets = []

    def display_events(self):
        print("\nAvailable Events:")
        for event, details in self.events.items():
            print(f"{event}: ${details['price']} per ticket, {details['seats']} seats available")

    def book_ticket(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event['seats'] >= quantity:
                total_price = event['price'] * quantity
                event['seats'] -= quantity
                self.booked_tickets.append({
                    "customer_id": customer.customer_id,
                    "event": event_name,
                    "quantity": quantity,
                    "total_price": total_price,
                })
                print(f"Successfully booked {quantity} tickets for {event_name}. Total price: ${total_price}")
            else:
                print(f"Not enough seats available for {event_name}. Only {event['seats']} seats left.")
        else:
            print(f"Event {event_name} not found.")

    def view_booked_tickets(self, customer):
        print("\nYour Booked Tickets:")
        customer_tickets = [t for t in self.booked_tickets if t["customer_id"] == customer.customer_id]
        if not customer_tickets:
            print("No tickets booked.")
        else:
            for ticket in customer_tickets:
                print(f"Event: {ticket['event']}, Quantity: {ticket['quantity']}, Total Price: ${ticket['total_price']}")


if __name__ == "__main__":
    booking_system = TicketBooking()

    print("Welcome to the Ticket Booking System!")
    customer_id = input("Enter your Customer ID: ")

    if Customer.verify_customer_id(customer_id):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        customer = Customer(customer_id, name, phone)
        print("Customer ID verified. Proceeding to ticket booking...")
    else:
        print("Invalid Customer ID. Please register.")
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        customer_id = Customer.generate_customer_id()
        customer = Customer(customer_id, name, phone)
        print(f"Your Customer ID is: {customer_id}")

    while True:
        print("\nTicket Booking Menu:")
        print("1. View Events")
        print("2. Book Ticket")
        print("3. View My Tickets")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            booking_system.display_events()
        elif choice == "2":
            event_name = input("Enter the event name: ")
            quantity = int(input("Enter the number of tickets: "))
            booking_system.book_ticket(event_name, quantity, customer)
        elif choice == "3":
            booking_system.view_booked_tickets(customer)
        elif choice == "4":
            print("Thank you for using the Ticket Booking System! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")
