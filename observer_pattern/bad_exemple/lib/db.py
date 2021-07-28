from hashlib import blake2b

users = []

class User:

    def __init__(self, name: str, password: str, email: str) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.plan = "basic"
        self.reset_code = ""

    def __repr__(self) -> str:
        return f"NAME : {self.name}, EMAIL: {self.email}, PASSWD: {self.password}"

    def reset_password(self, code: str, new_password: str):
        if code != self.reset_code:
            raise Exception("Invalid password reset code.")
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()

def create_user(name: str, password: str, email: str) -> User:
    new_user = User(name, password, email)
    users.append(new_user)
    return new_user

def find_user(email: str) -> User:
    for user in users:
        if user.email == email:
            return user
    raise Exception(f"User with email address {email} not found.")