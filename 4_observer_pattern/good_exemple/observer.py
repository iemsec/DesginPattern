from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan
from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_event_handlers

setup_slack_event_handlers()
setup_log_event_handlers()

register_new_user("eddy", "pass", "hello@gmail.com")

password_forgotten("hello@gmail.com")

upgrade_plan("hello@gmail.com")