from lib.stringtools import get_random_string
from lib.db import find_user, create_user
from .event import post_event

def register_new_user(name:str, password: str, email:str):
    user = create_user(name, password, email)

    post_event("user registred", user)

def password_forgotten(email: str):

    user = find_user(email)

    user.reset_code = get_random_string(16)

    post_event("password forgotten", user)
