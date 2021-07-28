from lib.stringtools import get_random_string
from lib.slack import post_slack_message
from lib.email import send_email
from lib.log import log
from lib.db import find_user, User, create_user

def register_new_user(name:str, password: str, email:str):
    user = create_user(name, password, email)

    post_slack_message("sales",
    f"{user.name} has registred with email address {user.email}. Spam it bro'")

    send_email(user.name, user.email,
        "Welcome",
        f"Thanks for registring, {user.name}! You're gonna love it. \nRegards,\nThe devNotes team")

    log(f"User registred with email address {user.email}")

def password_forgotten(email: str):

    user = find_user(email)

    user.reset_code = get_random_string(16)

    send_email(user.name, user.email,
        "Reset your password",
        f"To reset your password use this very secure code, {user.reset_code}! You're gonna love it. \nRegards,\nThe devNotes team")

    log(f"User with email address {user.email} requested a password reset")
