from settings import app
from views.test_db import *

app.add_url_rule('/get', methods=['GET'], view_func=get_users)
app.add_url_rule('/add', methods=['POST'], view_func=add_user)