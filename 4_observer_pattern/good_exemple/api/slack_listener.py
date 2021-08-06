from lib.slack import post_slack_message
from .event import subscribe

def handle_user_registred_event(user):
    post_slack_message("sales",
    f"{user.name} has registred with email address {user.email}. Spam it bro'")

def setup_slack_event_handlers():
    subscribe("user registred", handle_user_registred_event)
