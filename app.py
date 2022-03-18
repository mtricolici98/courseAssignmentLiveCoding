from flask import Flask

app = Flask('My app')
app.secret_key = b'123kjashlkdjhhlkj12h439188'  # Required for session to work


@app.route('/')
def main():
    return '<h1>Welcome to my hotel</h1>'


from views.web_view.RoomRoutes import rooms_view
from views.web_view.UserRoutes import user_views

app.register_blueprint(rooms_view)
app.register_blueprint(user_views)
