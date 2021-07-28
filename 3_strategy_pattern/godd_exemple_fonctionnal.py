import string
import random
from typing import Callable, List
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


def create_ordering_fifo(list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


def create_ordering_filo(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def create_ordering_random(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def __init__(self, ordering_strategy: Callable[[List[SupportTicket]],List[SupportTicket]]) -> None:
        self.ordering_strategy = ordering_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):

        list_copy = self.ordering_strategy(self.tickets)

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

app = CustomerSupport(create_ordering_random)

app.create_ticket("Foo", "I have tons of problem")
app.create_ticket("Bar", "Windows never work")
app.create_ticket("Jean", "I can't print anymore")
app.create_ticket("Marc", "The dishwasher make some noise")

app.process_tickets()