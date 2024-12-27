from abc import ABC, abstractmethod

class Customer:
    def __init__(self, name, ticket_number):
        """Initialize customer with name and ticket number."""
        self.name = name
        self.ticket_number = ticket_number

    def __str__(self):
        """String representation of the customer."""
        return f"Customer[Name: {self.name}, Ticket: {self.ticket_number}]"

class QueueOperations(ABC):
    @abstractmethod
    def enqueue(self, name):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def cancel_ticket(self, ticket_number):
        pass

    @abstractmethod
    def display_queue(self):
        pass

class TicketQueue(QueueOperations):
    def __init__(self):
        self.queue = []
        self.next_ticket_number = 1

    def enqueue(self, name):
        customer = Customer(name, self.next_ticket_number)
        self.queue.append(customer)
        self.next_ticket_number += 1
        print(f"Customer '{name}' has been added to the queue with Ticket #{customer.ticket_number}.")

    def dequeue(self):
        if self.queue:
            customer = self.queue.pop(0)
            print(f"Customer '{customer.name}' with Ticket #{customer.ticket_number} has been processed.")
        else:
            print("The queue is empty. No customers to process.")

    def cancel_ticket(self, ticket_number):
        for customer in self.queue:
            if customer.ticket_number == ticket_number:
                self.queue.remove(customer)
                print(f"Ticket #{ticket_number} for customer '{customer.name}' has been canceled.")
                return
        print(f"Ticket #{ticket_number} not found in the queue.")

    def display_queue(self):
        if not self.queue:
            print("The queue is empty.")
        else:
            print("Current queue:")
            for customer in self.queue:
                print(customer)

class TicketSystem:
    def __init__(self, queue):
        self.queue = queue

    def execute_command(self, command):
        if command == "add":
            name = input("Enter customer name: ").strip()
            self.queue.enqueue(name)
        elif command == "process":
            self.queue.dequeue()
        elif command == "cancel":
            try:
                ticket_number = int(input("Enter ticket number to cancel: "))
                self.queue.cancel_ticket(ticket_number)
            except ValueError:
                print("Invalid input. Please enter a valid ticket number.")
        elif command == "display":
            self.queue.display_queue()
        elif command == "exit":
            print("Exiting the system. Goodbye!")
            return False
        else:
            print("Invalid command. Please try again.")
        return True

if __name__ == "__main__":
    queue = TicketQueue()
    system = TicketSystem(queue)

    while True:
        command = input("\nEnter command (add/process/cancel/display/exit): ").strip().lower()
        if not system.execute_command(command):
            break

