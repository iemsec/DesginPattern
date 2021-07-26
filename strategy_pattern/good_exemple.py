import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy = random.shuffle(list_copy)
        return list_copy


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, strategy: TicketOrderingStrategy):

        list_copy = strategy.create_ordering(self.tickets)

        if len(list_copy) == 0:
            print("there are no tickets to process. Good Job !!!")
            return

        for ticket in list_copy:
            self.process_ticket(ticket)

    def process_ticket(self, ticket:SupportTicket):
        print("===========================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("===========================================")

app = CustomerSupport()

app.create_ticket("Foo", "I have tons of problem")
app.create_ticket("Bar", "Windows never work")
app.create_ticket("Jean", "I can't print anymore")
app.create_ticket("Marc", "The dishwasher make some noise")

app.process_tickets(RandomOrderingStrategy())