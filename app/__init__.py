from flask import Flask

app = Flask(__name__)

# Using bottom import as a workaround to circular imports which is common problem with Flask applications
from app import routes, api
