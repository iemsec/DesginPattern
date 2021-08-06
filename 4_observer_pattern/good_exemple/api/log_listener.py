from lib.log import log
from .event import subscribe

def handle_user_registred_event(user):
    log(f"User registred with email address {user.email}")

def handle_user_password_forgotten_event(user):
    log(f"User with email address {user.email} requested a password reset !")

def setup_log_event_handlers():
    subscribe("user registred", handle_user_registred_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
