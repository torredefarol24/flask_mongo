# Initialize App
from flask import Flask

app = Flask(__name__)

# Bootstrap Setup
from src.main.bootstrap import routes
