from flask import Flask
import os

template_folder = os.path.abspath("application/view/templates")
static_folde = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folde)

from application.controller import home_controller