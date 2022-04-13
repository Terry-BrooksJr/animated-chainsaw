import pytest
from flask_login import FlaskLoginClient
from flask import current_app as app 

app.test_client_class = FlaskLoginClient()
piop