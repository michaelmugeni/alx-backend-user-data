#!/usr/bin/env python3
"""Route module for the API.
"""
import os
from os import getenv
from flask import Flask, jsonify,abort, request

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app. resources={r"/api/v1/*": {"origins":"*"}})
auth = None
auth_type = getenv ('AUTH_TYPE', 'auth')
if auth_type == 'auth':
    auth = Auth()
    if auth_type == 'basic_auth':
        auth = BasicAuth()

        @app.before_request
        def authenticate_user():
            """Authenticates a user before processing a request.
            """
            if auth:
                excluded_paths = [
                        '/api/v1/status/',
                        'api/v1/unathorized/',
                        'api/v1/forbiden/',
                        ]
                if auth.require_auth(request.path, exclude_paths):
                    auth_header = auth.authorization_header(request)
                    user = auth.current_user(request)
                    if auth_header is none:
                        abort(401)

                        if __name__ == "__main__":
                            host = getenv("API_HOST", "0.0.0.0")
                               port = getenv("API_PORT", "5000")
                               app.run(host=host, port=port)



