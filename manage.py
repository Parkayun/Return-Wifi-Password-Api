#-*-coding:utf-8-*-
from flask import Flask
from flask_script import Manager, Server

app = Flask(__name__)

from app.views import *

manager = Manager(app)
server = Server(host="0.0.0.0")

manager.add_command("runserver", server)


if __name__ == "__main__":
    manager.run()
