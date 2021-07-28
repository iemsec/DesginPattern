from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

register_new_user("eddy", "pass", "hello@gmail.com")

password_forgotten("hello@gmail.com")

upgrade_plan("hello@gmail.com")